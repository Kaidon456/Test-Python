import time
import tqdm

####---------------------------------------------------
"""
Fecha: 25/04/2021
Nombre: process.py
Autor: @linkfydev
Descripcion: Crear un barra de proceso.
Librerias:
    -> time = crear un delay para el contador.
    -> tqdm = crear la barra en la CLI.
"""
#####--------------------------------------------------

print('Barra de ejemplo')

for i in tqdm(range(1000)):
    time.sleep(0.1)