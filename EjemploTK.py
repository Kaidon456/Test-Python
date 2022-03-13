from tkinter import *
from random import choice

####---------------------------------------------------
"""
Fecha: 13/03/2021
Nombre: EjmploTK.py
Autor: @mafervicas
Descripcion: Realiar una busqueda en Wikipedia y regresar en una UI
Librerias:
    ->  random = tomar aleatoriamente un numero de los ingresados.
    -> tkinter = generador para la UI.
"""
#####--------------------------------------------------

def seleccionar():
    entrada = (inp.get()).split(',')
    msg = Label(App, text=choice(entrada))
    msg.pack()

App = Tk()
App.title("ejemplo")
App.geometry("300x400")
inp = Entry(App)
inp.pack()

Boton = Button(App,text='Seleccionar',command=seleccionar)
Boton.pack()

App.mainloop()