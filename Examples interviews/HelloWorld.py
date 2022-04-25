
####---------------------------------------------------
"""
Fecha: 15/03/2021
Nombre: HelloWorld.py
Autor: @drkbugs
Descripcion: Buscar numeros repetidos en una Array.

Nota: este codigo es una daptacion de Javascript a python
"""
#####--------------------------------------------------

data = [1,1,2,2,3,4,4,4,5]
aux = [False,False,False,False,False]
ran = len(data) - 1
for i in range(ran):
    if not aux[data[i]]:
        aux[data[i]] = True
    else:
        print("Repetidos")