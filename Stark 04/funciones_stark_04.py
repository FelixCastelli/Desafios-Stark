import re
import os
import json

# 1.

def imprimir_dato(string: str) -> None:
    """
    Imprime el contenido del string en la consola.

    Args:
        string (str): El string que se va a imprimir.

    Returns:
        None
    """

    print(string)


def imprimir_menu_desafio_4() -> None:
    """
    Imprime el menú de opciones del desafío 4 en la consola.

    Returns:
        None
    """
    menu = f"""
*** Menu de opciones ***
A - Mostrar los nombres de los superheroes masculinos
B - Mostrar los nombres de las superheroes femeninas
C - Mostrar el superheroe masculino mas alto
D - Mostrar la superheroe femenina mas alta
E - Mostrar el superheroe masculino mas bajo
F - Mostrar la superheroe femenina mas baja
G - Mostrar la altura promedio de los superheroes masculinos
H - Mostrar la altura promedio de las superheroes femeninas
I - Mostrar el nombre del superheroe asociado a cada uno de los indicadores anteriores
J - Mostrar cantidad de superheroes por color de ojos
K - Mostrar cantidad de superheroes por color de pelo
L - Mostrar cantidad de superheroes por tipo de inteligencia
M - Mostrar los superheroes agrupados por color de ojos
N - Mostrar los superheroes agrupados por color de pelo
O - Mostrar los superheroes agrupados por tipo de inteligencia
Z - Salir
"""
    imprimir_dato(menu)


def stark_menu_principal_desafio_4():
    """
    Muestra el menú principal del desafío 4 y solicita al usuario que ingrese una opción.

    Returns:
        str: La opción ingresada por el usuario pasado a minusculas, o -1 si la opción no es válida.
    """
    imprimir_menu_desafio_4()

    opcion = input("Ingrese una de las opciones: ")

    valido = re.compile('[a-oA-OzZ]')

    if not valido.search(opcion):
        return -1
    else:
        return opcion.lower()


def stark_marvel_app_4(lista_heroes: list) -> None:
    """
    Ejecuta la aplicación principal del desafío stark 04.

    Args:
        lista_heroes (list): Lista de heroes.

    Returns:
        None
    """
    while True:
        opcion = stark_menu_principal_desafio_4()

        match opcion:
            case -1:
                os.system("cls")
                print("ERROR, opcion invalida, ingrese una opcion valida.")
                os.system("pause")
                continue
            case 'a':
                os.system("cls")
                stark_guardar_heroe_genero(lista_heroes, 'm')
                os.system("pause")
            case 'b':
                os.system("cls")
                stark_guardar_heroe_genero(lista_heroes, 'f')
                os.system("pause")
            case 'c':
                os.system("cls")
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "maximo", "altura", 'M')
                os.system("pause")
            case 'd':
                os.system("cls")
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "maximo", "altura", 'F')
                os.system("pause")
            case 'e':
                os.system("cls")
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "minimo", "altura", 'M')
                os.system("pause")
            case 'f':
                os.system("cls")
                stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, "minimo", "altura", 'F')
                os.system("pause")
            case 'g':
                os.system("cls")
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, 'M')
                os.system("pause")
            case 'h':
                os.system("cls")
                stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, 'F')
                os.system("pause")
            case 'i':
                pass
            case 'j':
                os.system("cls")
                stark_calcular_cantidad_por_tipo(lista_heroes, "color_ojos")
                os.system("pause")
            case 'k':
                os.system("cls")
                stark_calcular_cantidad_por_tipo(lista_heroes, "color_pelo")
                os.system("pause")
            case 'l':
                os.system("cls")
                stark_calcular_cantidad_por_tipo(lista_heroes, "inteligencia")
                os.system("pause")
            case 'm':
                os.system("cls")
                stark_listar_heroes_por_dato(lista_heroes, "color_ojos")
                os.system("pause")
            case 'n':
                os.system("cls")
                stark_listar_heroes_por_dato(lista_heroes, "color_pelo")
                os.system("pause")
            case 'o':
                os.system("cls")
                stark_listar_heroes_por_dato(lista_heroes, "inteligencia")
                os.system("pause")
            case 'z':
                os.system("cls")
                salir = input("Confirma salida? s/n: ")
                if salir == 's':
                    break
                os.system("pause")
                os.system("cls")


def leer_archivo(ruta: str) -> list:
    """
    Lee un archivo en modo lectura y carga su contenido en una lista de héroes.

    Args:
        ruta (str): Ruta del archivo a leer.

    Returns:
        list: Lista de héroes cargada desde el archivo.
    """
    with open(ruta, 'r') as file:
        lista_heroes = json.load(file)
    return lista_heroes


def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    """
    Guarda el contenido en un archivo con el nombre especificado.

    Args:
        nombre_archivo (str): Nombre del archivo a crear o sobrescribir.
        contenido (str): Contenido a guardar en el archivo.

    Returns:
        bool: True si se guarda el archivo correctamente, False en el caso contrario.
    """
    try:
        with open(nombre_archivo, 'w') as file:
            file.write(contenido)
    
        print(f"Se creo el archivo: {nombre_archivo}")
        return True
    except Exception:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza todas las palabras ingresadas.

    Args:
        texto (str): Palabras a capitalizar.

    Returns:
        str: Texto con todas las palabras capitalizadas.
    """
    texto_capitalizado = texto.title()
    return texto_capitalizado


def obtener_nombre_capitalizado(heroe: dict) -> str:
    """
    Obtiene el nombre capitalizado de un héroe.

    Args:
        heroe (dict): Diccionario de un heroe.

    Returns:
        str: Nombre del héroe, capitalizado.
    """
    nombre_heroe = capitalizar_palabras(heroe["nombre"])
    return f"Nombre: {nombre_heroe}"


def obtener_nombre_y_dato(heroe: dict, key: str) -> str:
    """
    Obtiene el nombre capitalizado del héroe y el dato correspondiente a una key.

    Args:
        heroe (dict): Diccionario de un heroe.
        key (str): key para conseguir el dato del héroe.

    Returns:
        str: Cadena de texto que combina el nombre capitalizado del héroe, la key en formato capitalizado y el valor de la key correspondiente.
    """
    nombre_heroe = obtener_nombre_capitalizado(heroe)
    return f"{nombre_heroe} | {key.capitalize()}: {heroe[key]}"

# 2.

def es_genero(heroe: dict, genero: str) -> bool:
    """
    Verifica si el género de un héroe coincide con el género buscado.

    Args:
        heroe (dict): Diccionario de un heroe.
        genero (str): Género a comparar.

    Returns:
        bool: True si el género del héroe coincide con el género buscado, False en el caso contrario.
    """
    if heroe["genero"] == genero.upper():
        return True
    else:
        return False


def stark_guardar_heroe_genero(lista_heroes: list, genero: str) -> bool:
    """
    Imprime y guarda en un archivo los nombres de los heroes que coinciden con el género especificado.

    Args:
        lista_heroes (list): La lista de heroes.
        genero (str): Género a evaluar. Puede ser "M" (masculino), "F" (femenino) o "NB" (no binario).

    Returns:
        bool: True si se guarda el archivo correctamente, False en caso contrario.
    """
    nombres = []

    for heroe in lista_heroes:
        if es_genero(heroe, genero):
            nombre_heroe = obtener_nombre_capitalizado(heroe)
            nombres.append(nombre_heroe)
            imprimir_dato(nombre_heroe)
    
    nombre_archivo = f"heroes_{genero.upper()}.csv"
    contenido = ','.join(nombres)
    return guardar_archivo(nombre_archivo, contenido)

# 3.

def calcular_min_genero(lista: list, key: str, genero: str) -> dict:
    """
    Encuentra el héroe o heroína con el valor mínimo para una clave específica, asdentro de una lista de héroes del género dado.

    Args:
        lista (list): La lista de héroes representada como una lista de diccionarios.
        key (str): Key sobre la cual se va a realizar la comparación para encontrar el valor mínimo.
        genero (str): Género de los héroes a respetar para la búsqueda del valor mínimo.

    Returns:
        dict: Diccionario del héroe o heroína que cumple con el valor mínimo para la key y genero especificada. Si no se encuentra ningún héroe que cumpla, se devuelve None.
    """
    flag_valor = False

    for heroe in lista:
        if es_genero(heroe, genero):
            if key in heroe:

                if not flag_valor:
                    valor_min = heroe[key]
                    heroe_min = heroe
                    flag_valor = True

                elif heroe[key] < valor_min:
                    valor_min = heroe[key]
                    heroe_min = heroe

    return heroe_min


def calcular_max_genero(lista: list, key: str, genero: str) -> dict:
    """
    Encuentra el héroe o heroína con el valor maximo para una clave específica, asdentro de una lista de héroes del género dado.

    Args:
        lista (list): La lista de héroes representada como una lista de diccionarios.
        key (str): Key sobre la cual se va a realizar la comparación para encontrar el valor maximo.
        genero (str): Género de los héroes a respetar para la búsqueda del valor maximo.

    Returns:
        dict: Diccionario del héroe o heroína que cumple con el valor maximo para la key y genero especificada. Si no se encuentra ningún héroe que cumpla, se devuelve None.
    """
    flag_valor = False

    for heroe in lista:
        if es_genero(heroe, genero):
            if key in heroe:

                if not flag_valor:
                    valor_max = heroe[key]
                    heroe_max = heroe
                    flag_valor = True

                elif heroe[key] > valor_max:
                    valor_max = heroe[key]
                    heroe_max = heroe

    return heroe_max


def calcular_max_min_datos_genero(lista: list, opcion: str, key: str, genero: str) -> dict:
    """
    Encuentra el héroe o heroína con el valor maximo para una clave específica, asdentro de una lista de héroes del género dado.

    Args:
        lista (list): La lista de héroes representada como una lista de diccionarios.
        opcion (str): Opción que indica si se debe buscar el valor máximo o mínimo.
        key (str): Key sobre la cual se va a realizar la comparación para encontrar el valor maximo o minimo.
        genero (str): Género de los héroes a respetar para la búsqueda del valor maximo o minimo.

    Returns:
        dict: Diccionario del héroe o heroína que cumple con el valor maximo o minimo para la key y genero especificada. Si no se encuentra ningún héroe que cumpla, se devuelve None.
    """
    if opcion == "maximo":
        heroe = calcular_max_genero(lista, key, genero)
    elif opcion == "minimo":
        heroe = calcular_min_genero(lista, key, genero)

    return heroe


def stark_calcular_imprimir_guardar_heroe_genero(lista: str, opcion: str, key: str, genero: str) -> bool:
    """
    Calcula, imprime y guarda el héroe con el valor máximo o mínimo de una key ingresada, basado en el género ingresado.

    Args:
        lista (str): La lista ingresada.
        opcion (str): Opción de cálculo: "minimo" o "maximo".
        key (str): Key sobre la cual realizar el cálculo.
        genero (str): Género del heroe a evaluar.

    Returns:
        bool: True si se guardo con exito el archivo csv y False si no se pudo guardar con exito.

    """
    heroe = calcular_max_min_datos_genero(lista, opcion, key, genero)
    dato_final = obtener_nombre_y_dato(heroe, key)
    if opcion == "minimo":
        imprimir_dato(f"Menor Altura: {dato_final}")
    else:
        imprimir_dato(f"Mayor Altura: {dato_final}")

    nombre_archivo = f"heroes_{opcion}_{key}_{genero}.csv"
    guardar_archivo(nombre_archivo, dato_final)

    return True

# 4.

def dividir(dividendo: float, divisor: int):
    if divisor == 0:
        return 0
    else:
        respuesta = dividendo / divisor
    return respuesta



def sumar_dato_heroe_genero(lista: list, key: str, genero: str) -> int:
    
    acumulador = 0

    for heroe in lista:
        if type(heroe) == dict and heroe != "" and heroe["genero"] == genero:
            acumulador += float(heroe[key])

    return acumulador


def cantidad_heroes_genero(lista_heroes: list, genero: str) -> int:

    acumulador = 0
    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            acumulador += 1

    return acumulador


def calcular_promedio_genero(lista: list, key: str, genero: str) -> float:

    acumulador = sumar_dato_heroe_genero(lista, key, genero)
    cantidad_heroes = cantidad_heroes_genero(lista, genero)

    promedio = dividir(acumulador, cantidad_heroes)

    return promedio


def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes: list, genero: str):
    if not lista_heroes:
        print("ERROR, lista de héroes vacía")
        return False
    else:
        promedio = calcular_promedio_genero(lista_heroes, "altura", genero)
        imprimir_dato(f"La altura promedio de los heroes de genero {genero} es: {promedio}")

        nombre_archivo = f"heroes_promedio_altura_{genero}.csv"
        contenido = f"Altura promedio del genero {genero.capitalize()}: {promedio}"
        if guardar_archivo(nombre_archivo, contenido):
            return True
        else:
            return False
        
# 5.

def calcular_cantidad_tipo(lista_heroes: list, key: str):
    if not lista_heroes:
        return ("ERROR, la lista se encuentra vacia")

    cantidad_tipo = {}
    for heroe in lista_heroes:
        if key in heroe:
            valor = heroe[key]
            valor_capitalizado = capitalizar_palabras(valor)
            if valor_capitalizado not in cantidad_tipo:
                cantidad_tipo[valor_capitalizado] = 1
            else:
                cantidad_tipo[valor_capitalizado] += 1

    return cantidad_tipo


def guardar_cantidad_heroes_tipo(tipo_dato: dict, dato: str):
    if not tipo_dato:
        print("ERROR, el tipo_dato está vacío")
        return False

    mensaje_final = ''
    for key in tipo_dato:
        valor = tipo_dato[key]
        mensaje = f"Caracteristica: {dato} {key} - Cantidad de heroes: {valor}\n"
        mensaje_final += mensaje

    nombre_archivo = f"heroes_cantidad_{dato}.csv"  
    return guardar_archivo(nombre_archivo, mensaje_final)


def stark_calcular_cantidad_por_tipo(lista_heroes: list, key: str) -> bool:
    cantidad_tipo = calcular_cantidad_tipo(lista_heroes, key)
    return guardar_cantidad_heroes_tipo(cantidad_tipo, key)

# 6.

def obtener_lista_de_tipos(lista_heroes: str, key: str):
    tipos = []

    for heroe in lista_heroes:
        if key in heroe:
            valor = heroe[key]
            if not valor:
                valor = 'N/A'
            else:
                valor = capitalizar_palabras(valor)
            tipos.append(valor)

    return set(tipos)


def normalizar_dato(dato: str, valor_default: str) -> str:
    if not dato:
        return valor_default
    return dato


def normalizar_heroe(heroe: dict, key: str) -> dict:
    if key in heroe:
        heroe[key] = capitalizar_palabras(normalizar_dato(heroe[key], "N/A"))
    heroe["nombre"] = capitalizar_palabras(heroe["nombre"])
    return heroe


def obtener_heroes_por_tipo(lista_heroes: list, variedades: set, tipo_dato: str) -> dict:
    heroes_por_tipo = {}

    for variedad in variedades:
        heroes_por_tipo[variedad] = []

    for heroe in lista_heroes:
        if tipo_dato in heroe:
            valor = normalizar_dato(heroe[tipo_dato], "N/A")
            if valor in variedades:
                heroes_por_tipo[valor].append(heroe["nombre"])

    return heroes_por_tipo


def guardar_heroes_por_tipo(heroes_por_tipo: dict, tipo_dato: str) -> bool:
    if not heroes_por_tipo:
        print("ERROR, el diccionario está vacío")
        return False

    mensaje_final = ''

    for tipo, heroes in heroes_por_tipo.items():
        if heroes:
            nombres = " | ".join(heroes)
            mensaje = f"{tipo_dato} {tipo}: {nombres}\n"
            mensaje_final += mensaje

    nombre_archivo = f"heroes_segun_{tipo_dato}.csv"
    return guardar_archivo(nombre_archivo, mensaje_final)


def stark_listar_heroes_por_dato(lista_heroes: list, tipo_dato: str) -> bool:
    tipos = obtener_lista_de_tipos(lista_heroes, tipo_dato)
    heroes_por_tipo = obtener_heroes_por_tipo(lista_heroes, tipos, tipo_dato)
    return guardar_heroes_por_tipo(heroes_por_tipo, tipo_dato)