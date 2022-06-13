
####--------------------------------------
"""
fecha: 07/10/2021
Nombre: algoritmos.py
Descripcion: ver el funcionamiento de varios añgoritmos.
Librrias:
    -
"""
####--------------------------------------

def pattern21(i:int):
    for x in range(1,i):
        for y in range(i,x-1,-1):
            print(y,end="")
        print()

def simple_piramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("")

def sum(n:int):
    total = 0
    for index in range(n+1):
        total += index
    return total

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n-1)

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

def triangulo(n):
    k = n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k -= 1
        for j in range(0,i+1):
            print("*",end=" ")
        print()