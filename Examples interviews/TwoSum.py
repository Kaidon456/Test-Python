###---------------------------------------------------
"""
Fecha: 18/03/2022
Nombre: TwoSum.py
Descripcion: Realizar la suma 10 basado en los numeros en un arreglo.
"""
#####--------------------------------------------------

def twosum(arr):
    r = len(arr)
    for i in range(r):
        for j in range(r):
            x,y=arr[i],arr[j]
            if (x+y)==10:
                print(f"la suma de las posiciones {i} y {j} es 10")

arr = [2,3,4,5,6]
twosum(arr)