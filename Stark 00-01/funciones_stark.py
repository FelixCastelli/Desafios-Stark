import os
from data_stark import lista_personajes

def menu_00():
    while True:
        os.system("cls")
        print("*** Menu De Opciones ***")
        print("-------------------------")
        print("1- Ver el nombre de los superheroes y sus alturas")
        print("2- Ver cual superheroe es el más alto")
        print("3- Ver cual superheroe es el más bajo")
        print("4- Ver la altura promedio entre todos los superheroes")
        print("5- Ver cual es el superheroe más pesado")
        print("6- Ver cual es el superheroes más liviano")
        print("7- Salir")

        try:
            opcion = int(input("Ingrese la opcion: "))

            while opcion < 1 or opcion > 7:
                opcion = int(input("ERROR, ingrese un numero que este dentro de las opciones: "))
        except ValueError:
            opcion = int(input("ERROR, eso no es un numero, ingrese un numero que este dentro de las opciones: "))
        return opcion
    

def elegir_opcion_00(opcion: int):
    os.system("cls")
    match opcion:
        case 1:
            imprimir_nombres_con_altura(lista_personajes, 'nombre', 'altura')
        case 2:
            print(f"El superheroe más alto es: {encontrar_max_min(lista_personajes, 'altura', 'nombre', True)}")
        case 3:
            print(f"El superheroe más bajo es: {encontrar_max_min(lista_personajes, 'altura', 'nombre', False, True)}")
        case 4:
            print(f"El promedio de altura entre todos los superheroes es: {encontrar_promedio(lista_personajes, 'altura'):.2f}cm")
        case 5:
            print(f"El superheroe más pesado es: {encontrar_max_min(lista_personajes, 'peso', 'nombre', True)}")
        case 6:
            print(f"El superheroe más liviano es: {encontrar_max_min(lista_personajes, 'peso', 'nombre', False, True)}")
        case 7:
            return opcion


def menu_01():        
    while True:
        os.system("cls")
        print("*** Menu De Opciones ***")
        print("-------------------------")
        print("1- Ver el nombre de los superheroes y sus alturas")
        print("2- Ver cual superheroe es el más alto")
        print("3- Ver cual superheroe es el más bajo")
        print("4- Ver la altura promedio entre todos los superheroes")
        print("5- Ver cual es el superheroe más pesado")
        print("6- Ver cual es el superheroes más liviano")
        print("7- Ver todos los superheroes de genero Masculino")
        print("8- Ver todos los superheroes de genero Femenino")
        print("9- Ver el superheroe masculino más alto")
        print("10- Ver la superheroe femenina más alta")
        print("11- Ver el superheroe masculino más bajo")
        print("12- Ver la superheroe femenina más baja")
        print("13- Ver el promedio de altura de los superheroes Masculinos")
        print("14- Ver el promedio de altura de las superheroes Femeninas")
        print("15- Ver los superheroes separados por color de ojos")
        print("16- Ver los superheroes separados por color de pelo")
        print("17- Ver los superheroes separados por tipo de inteligencia")
        print("18- Salir")

        try:
            opcion = int(input("Ingrese la opcion: "))

            while opcion < 1 or opcion > 18:
                opcion = int(input("ERROR, ingrese un numero que este dentro de las opciones: "))
        except ValueError:
            opcion = int(input("ERROR, eso no es un numero, ingrese un numero que este dentro de las opciones: "))
        return opcion


def elegir_opcion_01(opcion: int):
    os.system("cls")
    match opcion:
        case 1:
            imprimir_nombres_con_altura(lista_personajes, 'nombre', 'altura')
        case 2:
            print(f"El superheroe más alto es: {encontrar_max_min(lista_personajes, 'altura', 'nombre', True)}")
        case 3:
            print(f"El superheroe más bajo es: {encontrar_max_min(lista_personajes, 'altura', 'nombre', False, True)}")
        case 4:
            print(f"El promedio de altura entre todos los superheroes es: {encontrar_promedio(lista_personajes, 'altura'):.2f}cm")
        case 5:
            print(f"El superheroe más pesado es: {encontrar_max_min(lista_personajes, 'peso', 'nombre', True)}")
        case 6:
            print(f"El superheroe más liviano es: {encontrar_max_min(lista_personajes, 'peso', 'nombre', False, True)}")
        case 7:
            print(f"Los superheroes de genero masculino son:")
            lista_hombres = filtrar_lista(lista_personajes, 'M', 'genero', 'nombre')
            recorrer_lista(lista_hombres)
        case 8:
            print(f"Las superheroes de genero femenino son:")
            lista_mujeres = filtrar_lista(lista_personajes, 'F', 'genero', 'nombre')
            recorrer_lista(lista_mujeres)
        case 9:
            lista_hombres, lista_alturas = filtrar_lista(lista_personajes, 'M', 'genero', 'nombre', 'altura')
            print(f"El superheroe masculino más alto es: {encontrar_max_min_lista(lista_alturas, lista_hombres, True)}")
        case 10:
            lista_mujeres, lista_alturas = filtrar_lista(lista_personajes, 'F', 'genero', 'nombre', 'altura')
            print(f"La superheroe femenina más alta es: {encontrar_max_min_lista(lista_alturas, lista_mujeres, True)}")
        case 11:
            lista_hombres, lista_alturas = filtrar_lista(lista_personajes, 'M', 'genero', 'nombre', 'altura')
            print(f"El superheroe masculino más bajo es: {encontrar_max_min_lista(lista_alturas, lista_hombres, False, True)}")
        case 12:
            lista_mujeres, lista_alturas = filtrar_lista(lista_personajes, 'F', 'genero', 'nombre', 'altura')
            print(f"La superheroe femenina más baja es: {encontrar_max_min_lista(lista_alturas, lista_mujeres, False, True)}")
        case 13:
            a, lista_alturas = filtrar_lista(lista_personajes, 'M', 'genero', 'nombre', 'altura')
            print(f"El promedio de altura entre todos los superheroes masculinos es: {encontrar_promedio(lista_alturas, False):.2f}cm")
        case 14:
            a, lista_alturas = filtrar_lista(lista_personajes, 'F', 'genero', 'nombre', 'altura')
            print(f"El promedio de altura entre todas las superheroes femeninas es: {encontrar_promedio(lista_alturas, False):.2f}cm")
        # case 15:
        #     imprimir_lista_color_de_ojos(lista_personajes)
        # case 16:
        #     imprimir_lista_color_de_pelo(lista_personajes)
        # case 17:
        #     imprimir_lista_tipo_de_inteligencia(lista_personajes)
        case 18:
            return opcion


def imprimir_nombres_con_altura(lista: list, key: str, key2: str)-> None:
    print("----------------------------")
    for heroe in lista:
        print(f"Nombre: {heroe[key]}\nAltura: {float(heroe[key2]):.2f}cm")
        print("----------------------------")


def encontrar_max_min(lista: list, key: str, key2: str, maximo: bool = True, minimo:bool = False):
    flag_valor = True
    valor_final = None
    if maximo:
        for valor in lista:
            if flag_valor or float(valor[key]) > float(valor_temporal):
                nombre = valor[key2]
                flag_valor = False
                valor_temporal = valor[key]
            valor_final = float(valor_temporal)

    if minimo:
        for valor in lista:
            if flag_valor or float(valor[key]) < float(valor_temporal):
                nombre = valor[key2]
                flag_valor = False
                valor_temporal = valor[key]
            valor_final = float(valor_temporal)
    return nombre, valor_final


def encontrar_promedio(lista: list, key: str = False):
    contador = 0
    acumulador = 0
    if key: 
        for elemento in lista:
            acumulador += float(elemento[key])
            contador += 1
    else:
        for elemento in lista:
            acumulador += elemento
            contador += 1
    promedio = acumulador / contador
    return promedio


def filtrar_lista(lista: list, key: str, key2: str, key3: str, key4: str = False):
    lista_filtrada = []
    lista_filtrada_valores = []
    for elemento in lista:
        if key in elemento[key2]:
            lista_filtrada.append(elemento[key3])
            if key4:
                lista_filtrada_valores.append(float(elemento[key4]))
    return lista_filtrada, lista_filtrada_valores


def recorrer_lista(lista: list):
    print("-------------------------------")
    for persona in lista:
        print(persona)
        print("-------------------------------")


def encontrar_max_min_lista(lista: list, lista2: list, maximo: bool = True, minimo: bool = False):
    flag_valor = True
    valor_final = None
    contador_vueltas = 0
    if maximo:
        for valor in lista:
            if flag_valor or float(valor) > float(valor_temporal):
                contador_vueltas = contador_vueltas + 1
                flag_valor = False
                valor_temporal = valor
            valor_final = float(valor_temporal)

    if minimo:
        for valor in lista:
            if flag_valor or float(valor) < float(valor_temporal):
                contador_vueltas = contador_vueltas + 1
                flag_valor = False
                valor_temporal = valor
            valor_final = float(valor_temporal)
    nombre = lista2[contador_vueltas - 1]
    return nombre, valor_final