
####---------------------------------------------------
"""
Fecha: 15/03/2021
Nombre: FizzVuzz.py
Autor: @drkbugs
Descripcion: Imprimir los numeros divibles entre 3 con Buzz y 5 con Fizz, en
caso de ser entre ambos FizzBuzz, e imprimir el resto basado en un maximo.
"""
#####--------------------------------------------------


def fizzbuzz(max):
    for i in range(max):
        if i % 3==0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3==0:
            print("Fizz")
        if i % 5==0:
            print("Buzz")
        else:
            print(i)

fizzbuzz(45)