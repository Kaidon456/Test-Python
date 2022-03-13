import pyautogui as auto
from time import sleep

####---------------------------------------------------
"""
Fecha: 19/10/2021
Nombre: spam.py
Descripcion: fungir como escritura y envio constante x mensaje
Librerias:
    -> pyautogui = escribir y mandar mensaje en la textbox actual.
    -> time = uso unico para invocar a sleep en tiempos definidos.
"""
#####--------------------------------------------------

print('Inicializando...')
sleep(5)
while True:
    auto.typewrite("Intro a farmear exp I")
    auto.press("enter")
    sleep(61)
