import pyautogui as auto
from time import sleep

####---------------------------------------------------
"""
Fecha: 07/10/2021
Nombre: spam.py
Descripcion: fungor como escritura y envio constante x mensaje
Librerias:
    -> pyautogui = escribir y mandar mensaje en la textbox actual.
    -> time = uso unico para invocar a sleep en tiempos definidos.
"""
#####--------------------------------------------------
while True:
    sleep(10)
    auto.write("wachen lo que descubri XD")
    auto.press("enter")