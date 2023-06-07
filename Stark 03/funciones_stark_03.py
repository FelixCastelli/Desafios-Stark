import re
import os

def extraer_iniciales(nombre_heroe: str) -> str:
    """
    Extrae las iniciales de un nombre de heroe ingresado.

    Args:
        nombre_heroe (str): El nombre del heroe.

    Returns:
        str: Las iniciales del nombre del heroe en formato "X.X.".
    """
    if not nombre_heroe:
        return 'N/A'
    
    else:
        iniciales = []
        nombre_separado = nombre_heroe.replace('-', ' ').split()

        for inicial in nombre_separado:
            if inicial.lower() == "the":
                pass
            else:
                iniciales.append(inicial[0])

        return f"{'.'.join(iniciales).upper()}."


def definir_iniciales_nombre(heroe: dict) -> bool:
    """
    Agrega las iniciales del nombre del heroe a una nueva clave llamada "iniciales".

    Args:
        heroe (dict): El diccionario del heroe ingresado.

    Returns:
        bool: False o True dependiendo de si se cumplen las condiciones o no.
    """
    if type(heroe) != dict or "nombre" not in heroe:
        return False
    else:
        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
        return True


def agregar_iniciales_nombre(lista_heroes: list) -> bool:
    """
    Itera la lista ingresada y llama a la funcion definir_iniciales_nombre si se cumplen los requisitos.

    Args:
        lista_heroes (list): La lista de heroes para iterar

    Returns:
        bool: False o True dependiendo de si se cumplen las condiciones o no.
    """
    if type(lista_heroes) != list or not lista_heroes:
        return False
    else:
        for heroe in lista_heroes:
            retorno = definir_iniciales_nombre(heroe)
            if not retorno:
                print("El origen de datos no contiene el formato correcto")
                return False
        
        return True


def stark_imprimir_nombres_con_iniciales(lista_heroes: list) -> str:
    """
    Imprime el nombre de los heroes con este formato: "* Nombre (Iniciales)".

    Args:
        lista_heroes (list): Lista de heroes ingresada.

    Returns:
        None
    """

    if type(lista_heroes) != list or not lista_heroes:
        return False

    retorno = agregar_iniciales_nombre(lista_heroes)

    if retorno:
        for heroe in lista_heroes:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")
    else:
        print("El origen de los datos no contiene el formato correcto")


def generar_codigo_heroe(id_heroe: int, genero_heroe: str) -> str:
    """
    Genera el código del héroe en base al ID y género recibidos.

    Args:
        id_heroe (int): ID del héroe.
        genero_heroe (str): Género del héroe ('M', 'F' o 'NB').

    Returns:
        str: Código generado del héroe con un máximo de 10 caracteres.
             En caso de no pasar las validaciones, devuelve 'N/A'.
    """
    if type(id_heroe) != int or genero_heroe.upper() not in ('M', 'F', 'NB'):
        return 'N/A'
    else:
        codigo = "{genero}-{id:08}".format(genero=genero_heroe.upper(), id=id_heroe) # Esto es lo que pude encontrar para hacer que se rellene de ceros adelante
        return codigo[:10]


def agregar_codigo_heroe(heroe: dict, id_heroe: int) -> bool:
    """
    Agrega el código del héroe al diccionario 'heroe' usando la función 'generar_codigo_heroe'.

    Args:
        heroe (dict): Diccionario con los datos del heroe.
        id_heroe (int): ID del héroe.

    Returns:
        bool: True si se agregó el código correctamente, False si no se cumplio la verificacion.
    """
    codigo = generar_codigo_heroe(id_heroe, heroe["genero"])
    if not heroe or len(codigo) != 10:
        return False
    else:
        heroe["codigo_heroe"] = codigo
        return True


def stark_generar_codigos_heroes(lista_heroes: list) -> None:
    """
    Genera y asigna códigos de héroe a cada personaje de la lista de heroes, muestra la cantidad de códigos generados, así como el código del primer y último héroe.

    Args:
        lista_heroes (list): Lista de heroes.

    Returns:
        None
    """
    posicion = 0
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")

    for heroe in lista_heroes:
        if type(heroe) != dict or not heroe["genero"]:
            print("El origen de datos no contiene el formato correcto")
        else:
            agregar_codigo_heroe(heroe, posicion)
            posicion += 1
    print(f"""
Se asignaron {posicion} codigos
El código del primer héroe es: {lista_heroes[0]["codigo_heroe"]}
El código del del último héroe es: {lista_heroes[-1]["codigo_heroe"]} 
""")
    

def sanitizar_entero(numero_str: str) -> int:
    """
    Analiza un string y determina si es un entero positivo.

    Args:
        numero_str (str): El string al que va a analizar si es un entero.

    Returns:
        int: El valor de retorno segun el problema que fue encontrado:
             -1: Si tiene caracteres no numericos.
             -2: Si el numero es negativo.
             -3 Si ocurre algun otro error que no deje convertirlo a entero.
             El numero transformado a entero si no ocurrio ningun problema.
    """
    numero_str = numero_str.strip()
    try:
        numero = int(numero_str)
        if numero < 0:
            return -2
        else:
            return numero
    except ValueError:
        return -1
    except:
        return -3


def sanitizar_flotante(numero_str: str) -> float:
    """
    Analiza un string y determina si es un flotante positivo.

    Args:
        numero_str (str): El string al que va a analizar si es un flotante.

    Returns:
        float: El valor de retorno segun el problema que fue encontrado:
             -1: Si tiene caracteres no numericos.
             -2: Si el numero es negativo.
             -3 Si ocurre algun otro error que no deje convertirlo a flotante.
             El numero transformado a flotante si no ocurrio ningun problema.
    """
    numero_str = numero_str.strip()
    try:
        numero = float(numero_str)
        if numero < 0:
            return -2
        else:
            return numero
    except ValueError:
        return -1
    except:
        return -3


def sanitizar_string(valor_str: str, valor_por_defecto: str = '-') -> str:
    """
    Analiza un string y determina si es un string, si lo es le saca las '/' y lo devuelve en minuscula.

    Args:
        valor_str (str): El string al que va a analizar si es un string sin numeros.

    Returns:
        str: Si el string tiene numeros devueve 'N/A'.
             Si el string era vacio, devuelve el valor por defecto.
             Si el string se verifico devuelve el string sin '/' pasado todo a minuscula.
    """
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    numero = re.compile('[0-9]')
    barra = re.compile('/')
    
    if numero.search(valor_str):
        return 'N/A'
    
    else:
        if barra.search(valor_str):
            valor_str = valor_str.replace('/', ' ')

        if not valor_str:
            return valor_por_defecto.lower()
        
        else:
            return valor_str.lower()


def sanitizar_dato(heroe: dict, key: str, tipo_dato: str) -> bool:
    """
    Sanitiza un dato específico de un heroe en el diccionario.

    Args:
        heroe (dict): El diccionario que contiene los datos del héroe.
        key (str): La clave del dato que se va a sanitizar.
        tipo_dato (str): El tipo de dato que se espera para el valor.

    Returns:
        bool: True si el dato se sanitizó correctamente, False en caso contrario.
    """
    if key not in heroe:
        print("La clave especificada no existe en el heroe")
        return False
    
    match tipo_dato:
        case 'string':         
            heroe[key] = sanitizar_string(heroe[key])
        case 'entero':
            heroe[key] = sanitizar_entero(heroe[key])
        case 'flotante':
           heroe[key] = sanitizar_flotante(heroe[key])
        case _:
            print("Tipo de dato no reconocido")
            return False
    
    return True


def stark_normalizar_datos(lista_heroes: list) -> None:
    """
    Normaliza los datos de los héroes en una lista.

    Recorre la lista de héroes y sanitiza los valores de las siguientes claves:
    'altura', 'peso', 'color_ojos', 'color_pelo', 'fuerza' e 'inteligencia'.

    Args:
        lista_heroes (list): La lista de heroes.

    Returns:
        None
    """
    if not lista_heroes:
        print("ERROR: Lista de heroes vacia")
        return
    for heroe in lista_heroes:
        sanitizar_dato(heroe, "altura", "flotante")
        sanitizar_dato(heroe, "peso", "flotante")
        sanitizar_dato(heroe, "color_ojos", "string")
        sanitizar_dato(heroe, "color_pelo", "string")
        sanitizar_dato(heroe, "fuerza", "entero")
        sanitizar_dato(heroe, "inteligencia", "entero")
    
    print("Datos normalizados")


def generar_indice_nombres(lista_heroes: list) -> list:
    """
    Genera una lista de palabras que componen los nombres de los personajes.

    Args:
        lista_heroes (list): La lista de heroes.

    Returns:
        list: Una lista con las palabras que componen los nombres de los personajes.
    """
    lista_nombres = []
    if not lista_heroes:
        print("El origen de datos no contiene el formato correcto")

    for heroe in lista_heroes:
        if type(heroe) != dict or "nombre" not in heroe:
            print("El origen de datos no contiene el formato correcto")

        
        lista_nombres += (heroe['nombre'].split())
    
    return lista_nombres


def stark_imprimir_indice_nombre(lista_heroes: list):
    """
    Muestra por pantalla el índice de nombres generado por la función generar_indice_nombres.

    Args:
        lista_heroes (list): La lista de personajes.

    """
    indice_nombres = generar_indice_nombres(lista_heroes)
    indice_separado = '-'.join(indice_nombres)
    print(indice_separado)


def convertir_cm_a_mtrs(valor_cm: float) -> float:
    """
    Convierte un valor en centímetros a metros.

    Args:
        valor_cm (float): El valor en centímetros a convertir.

    Returns:
        float: El valor convertido a metros si el valor es un numero flotante, de lo contrario retorna -1.

    """

    if type(valor_cm) != float or valor_cm < 0:
        return -1
    else:
        valor_mtrs = valor_cm / 100
        return valor_mtrs


def generar_separador(patron: str, largo: int, imprimir: bool = True) -> str:
    """
    Genera un separador usando el patron dado.

    Args:
        patron (str): El carácter que se va a utilizar como patrón para generar el separador.
        largo (int): El número de veces que se va a repetir el patrón para formar el separador.
        imprimir (bool, optional): Indica si se debe imprimir el separador. Es True por defecto.

    Returns:
        str: El separador generado.
    """
    if not patron or len(patron) > 2 or type(largo) != int or largo < 1 or largo > 235:
        return 'N/A'
    separador = patron * largo
    if not imprimir:
        return separador
    else:
        print(separador)
        return separador


def generar_encabezado(titulo: str) -> str:
    """
    Genera un encabezado con el título dado.

    Args:
        titulo (str): El título que se va a usar en el encabezado.

    Returns:
        str: El encabezado generado.
    """
    separador = generar_separador('*', 100, False)
    return f"""
{separador}
{titulo.upper()}
{separador}
"""


def imprimir_ficha_heroe(heroe: dict) -> None:
    """
    Imprime la ficha de un héroe con su información detallada.

    Args:
        heroe (dict): Un diccionario que contiene la información de cada heroe.

    Returns:
        None
    """
    print(f"""
{generar_encabezado("principal")}
NOMBRE DEL HÉROE: {heroe["nombre"]} {heroe["iniciales"]}

IDENTIDAD SECRETA: {heroe["identidad"]}

CONSULTORA: {heroe["empresa"]}

CÓDIGO DE HÉROE: {heroe["codigo_heroe"]}
{generar_encabezado("fisico")}
ALTURA: {heroe["altura"]} Mtrs.

PESO: {heroe["peso"]} Kg.

FUERZA: {heroe["fuerza"]} N
{generar_encabezado("señas particulares")}
COLOR DE OJOS: {heroe["color_ojos"]}

COLOR DE PELO: {heroe["color_pelo"]}
""")


def stark_navegar_fichas(lista_heroes: list):
    """
    Navega por las fichas de los héroes en una lista.

    Muestra la ficha del primer héroe en la lista y despues ofrece varias opciones:
    [ 1 ] Ir a la izquierda: Muestra la ficha del héroe anterior en la lista.
    [ 2 ] Ir a la derecha: Muestra la ficha del héroe siguiente en la lista.
    [ S ] Salir: Termina la navegación y finaliza la función.

    Args:
        lista_heroes (list): La lista de héroes.

    Returns:
        None
    """
    numero_heroe = 0

    imprimir_ficha_heroe(lista_heroes[numero_heroe])

    while True:
        opcion = input("[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir: ")
        while opcion not in ['1', '2', 'S']:
            opcion = input("ERROR, esa no es una opcion valida, ingrese: [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir: ")
        match opcion:
            case '1':
                os.system("cls")
                imprimir_ficha_heroe(lista_heroes[numero_heroe - 1])
                numero_heroe -= 1
            case '2':
                os.system("cls")
                imprimir_ficha_heroe(lista_heroes[numero_heroe + 1])
                numero_heroe += 1
            case 'S':
                os.system("pause")
                break


def validar_entero(numero: str) -> bool:
    """
    Valida si una cadena de texto representa un número entero válido.

    Args:
        numero (str): La cadena de texto a validar.

    Returns:
        bool: True si la cadena representa un número entero válido, False en el caso contrario.
    """
    if numero.isdigit():
        return True
    else:
        return False


def imprimir_menu() -> None:
    """
    Imprime el menú de opciones en la consola.

    Returns:
        None
    """
    print("""
*** Menu de opciones ***
1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
6 - Salir
""")


def stark_menu_principal() -> int:
    """
    Muestra el menú principal y solicita al usuario que ingrese una opción.

    Returns:
        int: La opción ingresada por el usuario, si la opción no es un número entero, se devuelve -1.
    """
    imprimir_menu()

    opcion = input("Ingrese la opcion: ")

    respuesta = validar_entero(opcion)

    if respuesta == True:
        opcion = int(opcion)
    elif respuesta == False:
        return -1

    return opcion


def stark_marvel_app_3(lista_heroes: list) -> None:
    """
    Ejecuta la aplicación principal de stark.

    Args:
        lista_heroes (list): Una lista de héroes.

    Returns:
        None
    """
    while True:
        os.system("cls")
        opcion = stark_menu_principal()

        if opcion == -1 or opcion < 1 or opcion > 6:
            os.system("cls")
            print("ERROR, opcion invalida, ingrese una opcion valida.")
            os.system("pause")
            continue
        
        match opcion:
            case 1:
                os.system("cls")
                stark_imprimir_nombres_con_iniciales(lista_heroes)
                os.system("pause")
            case 2:
                os.system("cls")
                stark_generar_codigos_heroes(lista_heroes)
                os.system("pause")
            case 3:
                os.system("cls")
                stark_normalizar_datos(lista_heroes)
                os.system("pause")
            case 4:
                os.system("cls")
                stark_imprimir_indice_nombre(lista_heroes)
                os.system("pause")
            case 5:
                os.system("cls")
                stark_navegar_fichas(lista_heroes)
                os.system("pause")
            case 6:
                os.system("cls")
                salir = input("Confirma salida? s/n: ")
                if salir == 's':
                    break