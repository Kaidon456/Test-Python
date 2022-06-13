import time
from tqdm import tqdm

####---------------------------------------------------
"""
Fecha: 13/06/2022
Nombre: process.py
Autor: @linkfydev
Descripcion: Crear un barra de proceso.
Librerias:
    -> time = crear un delay para el contador.
    -> tqdm = crear la barra en la CLI.
"""
#####--------------------------------------------------

print('Barra de ejemplo')

for i in tqdm(range(0, 100), desc ="Testing"):
    time.sleep(.1)
