import time
import dht
import machine
import network
import urequest

WIFI_SSID = ''     #nome_da_rede_wifi
WIFI_PASSWORD = '' #senha_da_rede_wifi
DHT4_PIN = 4       #GPIO da placa
API_KEY =''        #Chave para a API do thingspeak para gravação de dados
TIME_SLEEP = 900   #Tempo entre uma leitura e outra 15 minutos

def connect_wifi():
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to WiFi...')
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            time.sleep(1)
    print('Network config:', sta_if.ifconfig())

def mesure_temperature_and_humidity():
        d = dht.DHT22(machine.Pin(DHT4_PIN))
        d.measure()
        t = d.temperature()
        h = d.humidity()
        print('temperature = %.2f' % t)
        print('humidity    = %.2f' % h)
        print('send data to ThingSpeak')
        data_thingspeak="https://api.thingspeak.com/update?api_key=%s&field1=%s&field2=%s" %(API_KEY,t,h)
        urequest.urlopen(data_thingspeak)
   
while True:
        connect_wifi()
        mesure_temperature_and_humidity()
        time.sleep(TIME_SLEEP)
