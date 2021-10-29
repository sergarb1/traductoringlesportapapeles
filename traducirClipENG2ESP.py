#!/usr/bin/python3

'''
Para la traduccion
pip3 install deep-translator

Documentación biblioteca
pip3 install pyperclip
https://pyperclip.readthedocs.io/en/latest/
Si da "Not implemented Error"
sudo apt-get install curl #to install curl
sudo apt-get install xsel #to install the xsel utility.
sudo apt-get install xclip #to install the xclip utility.
pip install gtk #to install the gtk Python module.
pip install PyQt4 #to install the PyQt4 Python modu

'''


from deep_translator import GoogleTranslator

import pyperclip as pc

import time


while True:
    tmp_value= pc.waitForNewPaste()
    time.sleep(0.1)
    #Obtenemos datos del portapapeles
    datos = pc.paste().strip()
    #Impresion de depuracion print(datos)
    #Traducimos
    traduccion = GoogleTranslator(source='en', target='es').translate(datos)  # output -> Weiter so, du bist großarti
    #Impresion de depuracion print(traduccion)
    pc.copy(traduccion)
