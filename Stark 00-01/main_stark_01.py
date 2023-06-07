import os
from funciones_stark import *

while True:
    x = menu_01()
    y = elegir_opcion_01(x)

    if y == 18:
        salir = input("Confirma salida? s/n: ")
        if salir == 's':
            break

    os.system("pause")