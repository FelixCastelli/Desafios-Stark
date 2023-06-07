import os
from funciones_stark import *

while True:
    x = menu_00()
    y = elegir_opcion_00(x)

    if y == 7:
        salir = input("Confirma salida? s/n: ")
        if salir == 's':
            break

    os.system("pause")