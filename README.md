# Micropython
Utilização de placa nodemcu com micropython e sensor (DHT22) de temperatura e umidade para envio de dados para o site thingspeak.com

**1 - Preparar o ambiente**

    1.1 - Criar o ambiente virtual (python3)
        1.1.1 - virtualenv <ambiente_virtual>
        1.1.2 - cd <ambiente_virtual>
        1.1.3 - source bin/activate
        1.1.4 - buscar o firmware para o nodemcu em http://micropython.org/download#esp8266 e gravar no diretorio <ambiente_vritual>
        1.1.5 - pip install esptool
        1.1.6 - conectar o nodemcu no computador
        1.1.7 - verifique em que porta a placa está conectada (/dev/ttyUBSB0|1 ?)
        1.1.8 - esptool.py --port /dev/ttyUSB? erase_flash para apagar o que está placa
        1.1.9 - esptool.py --port /dev/ttyUSB/ --baud 460800 write_flash --flash_size=detect 0 <nome do firmware baixado no passo 1.1.4>
        1.1.10 - pip install adafruit-ampy
        1.1.11 - ampy --port /dev/ttyUSB? ls  (deve responder mostrando o boot.py
        1.1.12 - pip install jupyter
        1.1.13 - git clone https://github.com/goatchurchprime/jupyter_micropython_kernel.git
        1.1.14 - pip install -e jupyter_micropython_kernel
        1.1.15 - python -m jupyter_micropython_kernel.install
        1.1.16 - jupyter kernelspec list (deve mostrar linhas, uma delas referendando o micropython
        1.1.17 - jupyter notebbok
        1.1.18 - new micropython - USB
        1.1.19 - na primeira linha do notebbok digitar %serialconnect to --port=/dev/ttyUSB? --baud=115200 e CTRL+ENTER


**2 - Inserir o códigos**

    2.1 - Inserir no nodemcu pelo ampy a biblioteca urllib.request ( https://github.com/micropython/micropython-lib/blob/master/urllib.urequest/urllib/urequest.py)
        2.1.1 - Salvar o código urequest.py no <ambiente_virtual> 
        2.1.2 - Carregar a biblioteca ampy --port /dev/ttyUSB? put urequest.py
        2.1.3 - ampy --port /dev/ttyUSB? ls  (deve responder mostrando o boot.py e urequest.py
    2.2 - Utilizar o código deste projeto
    
**3 - Gravar o código no microprocessador nodemcu**

        3.1 - Salvar o código  deste projeto ou aquele testado no jupyter como main.py
        3.2 - Gravar o main.py no nodemcu   `ampy --port /dev/ttyUSB0 put main.py`
        3.3 - Lista módulos gravados no nodemcu `ampy --port /dev/ttyUSB0 ls`  (Deverá listar boot.py, main.py e urequest.py)

        



        
