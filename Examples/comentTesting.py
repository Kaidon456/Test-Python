
####---------------------------------------------------
"""
Fecha: 13/03/2021
Nombre: comentTesting.py
Autor: @codigofacilito.oficial
Descripcion: Realizar pruebas mediante el uso de Doctest.
"""
#####--------------------------------------------------
'''CMD -> python -m doctest (modulo)'''

def suma(a,b):
    """
    Retorna la suma de A y B

    >>> suma(1,1)
    2

    >>> suma(10,10)
    25

    >>> suma(100,200)
    300
    """
    return a+b