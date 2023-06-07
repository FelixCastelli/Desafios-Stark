import os
def stark_normalizar_datos(lista: list) -> None:
    """
    Normaliza los valores numéricos en todas las keys de los diccionarios en la lista de héroes.

    Args:
        lista (list): La lista de heroes.

    Returns:
        None
    """
    if not lista:
        print("ERROR: Lista de héroes vacía")
        return

    datos_modificados = False

    for heroe in lista:
        if isinstance(heroe, dict): # El isinstance es la unica manera que encontre de poder hacerlo
            for key, value in heroe.items():
                if isinstance(value, str) and value.isdigit():
                    heroe[key] = int(value)
                    datos_modificados = True

    if datos_modificados:
        print("Se han normalizado los valores numéricos en todas las claves")

# Ej 1 #00:

def obtener_nombre(lista: list):
    return f"Nombre: {lista['nombre']}".title()


def imprimir_dato(string: str):
    print(string)
        

def stark_imprimir_nombres_heroes(lista: list):
    if not lista:
         return -1
    else:
        for heroe in lista:
            nombre = obtener_nombre(heroe)
            imprimir_dato(nombre)

# Ej 2 #00:

def obtener_nombre_y_dato(lista: list, key: str):
        nombre = obtener_nombre(lista)
        return f"{nombre} | {key}: {lista[key]}".title()
    

def stark_imprimir_nombres_alturas(lista: list):
    if not lista:
        return -1
    else:
        for heroe in lista:
            nombre_y_dato = obtener_nombre_y_dato(heroe, 'altura')
            imprimir_dato(nombre_y_dato)

# Ej 3, 4, 6, 7 #00:

def calcular_max(lista: list, key: str):
    flag_valor = False

    for heroe in lista:
        if key in heroe:

            if not flag_valor:
                valor_max = heroe[key]
                heroe_max = heroe
                flag_valor = True

            elif heroe[key] > valor_max:
                valor_max = heroe[key]
                heroe_max = heroe

    return heroe_max


def calcular_min(lista: list, key: str):
    flag_valor = False

    for heroe in lista:
        if key in heroe:

            if not flag_valor:
                valor_min = heroe[key]
                heroe_min = heroe
                flag_valor = True

            elif heroe[key] < valor_min:
                valor_min = heroe[key]
                heroe_min = heroe

    return heroe_min


def calcular_max_min_datos(lista: list, opcion: str, key: str):
    if opcion == 'maximo':
        heroe = calcular_max(lista, key)
    elif opcion == 'minimo':
        heroe = calcular_min(lista, key)

    return heroe


def stark_calcular_imprimir_heroe(lista: str, opcion: str, key: str):
    heroe = calcular_max_min_datos(lista, opcion, key)
    dato_final = obtener_nombre_y_dato(heroe, key)
    imprimir_dato(dato_final)

# Ej 5 #00:

def sumar_dato_heroe(lista: list, key: str):
    acumulador = 0

    for heroe in lista:
        if type(heroe) == dict and heroe != "":
            acumulador += float(heroe[key])

    return acumulador


def dividir(dividendo: float, divisor: float):
    if divisor == 0:
        return 0
    else:
        respuesta = dividendo / divisor
    return respuesta


def calcular_promedio(lista: list, key: str):
    contador = 0

    for heroe in lista:
        if heroe:
            contador += 1

    acumulador = sumar_dato_heroe(lista, key)

    promedio = dividir(acumulador, contador)

    return promedio


def stark_calcular_imprimir_promedio_altura(lista: list):
    if not lista:
        return -1
    promedio = calcular_promedio(lista, 'altura')

    imprimir_dato(promedio)

def imprimir_menu():
    menu = """
*** Menu De Opciones ***
-------------------------
1- Ver el nombre de los superhéroes y sus alturas
2- Ver cuál superhéroe es el más alto
3- Ver cuál superhéroe es el más bajo
4- Ver la altura promedio entre todos los superhéroes
5- Ver cuál es el superhéroe más pesado
6- Ver cuál es el superhéroe más liviano
7- Salir
"""

    imprimir_dato(menu)

def validar_entero(numero: str):
    if numero.isdigit():
        return True
    else:
        return False

def stark_menu_principal():
    imprimir_menu()

    opcion = input("Ingrese la opcion: ")

    respuesta = validar_entero(opcion)

    if respuesta == True:
        opcion = int(opcion)
    elif respuesta == False:
        return -1

    return opcion

def stark_marvel_app(lista: list):

    while True:
        os.system("cls")
        opcion = stark_menu_principal()

        if opcion == -1 or opcion < 1 or opcion > 7:
            os.system("cls")
            print("ERROR, opcion invalida, ingrese una opcion valida.")
            os.system("pause")
            continue

        stark_normalizar_datos(lista)

        match opcion:
            case 1:
                os.system("cls")
                stark_imprimir_nombres_alturas(lista)
                os.system("pause")
            case 2:
                os.system("cls")
                stark_calcular_imprimir_heroe(lista, 'maximo', 'altura')
                os.system("pause")
            case 3:
                os.system("cls")
                stark_calcular_imprimir_heroe(lista, 'minimo', 'altura')
                os.system("pause")
            case 4:
                os.system("cls")
                stark_calcular_imprimir_promedio_altura(lista)
                os.system("pause")
            case 5:
                os.system("cls")
                stark_calcular_imprimir_heroe(lista, 'maximo', 'peso')
                os.system("pause")
            case 6:
                os.system("cls")
                stark_calcular_imprimir_heroe(lista, 'minimo', 'peso')
                os.system("pause")
            case 7:
                os.system("cls")
                salir = input("Confirma salida? s/n: ")
                if salir == 's':
                    break
                os.system("pause")
                os.system("cls")