import algoritmos as algo
from time import sleep

while True:
    print("-------Opciones--------")
    print("1) pattern21")
    print("2) piramide simple")
    print("3) sum")
    print("4) countdown")
    print("5) factorial")
    print("6) fibonacci")
    print("7) triangulo")
    print("0) salir")
    opc = int(input("ESCOJA SU OPCION: "))
    if opc < 0 or opc > 7:
        print("Opcion no disponible")
    elif opc == 0:
        print("saliendo del programa")
        sleep(5)
        break
    else:
        if opc == 1:
            print()
            n = int(input("ingrese un numero: "))
            algo.pattern21(n)
            sleep(3)
            print()
        if opc == 2:
            print()
            n = int(input("ingrese un numero: "))
            algo.simple_piramid(n)
            sleep(3)
            print()
        if opc == 3:
            print()
            n = int(input("ingrese un numero: "))
            algo.sum(n)
            sleep(3)
            print()
        if opc == 4:
            print()
            n = int(input("ingrese un numero: "))
            algo.countdown(n)
            sleep(3)
            print()
        if opc == 5:
            print()
            n = int(input("ingrese un numero: "))
            print(f"factorial de {n} es {algo.factorial(n)}")
            sleep(3)
            print()
        if opc == 6:
            print()
            n = int(input("ingrese un numero: "))
            for i in range(n):
                print(algo.fibonacci(i))
            sleep(3)
            print()
        if opc == 7:
            print()
            n = int(input("ingrese un numero: "))
            algo.triangulo(n)
            sleep(3)
            print()

