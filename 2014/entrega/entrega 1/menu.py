"""
Parte II ­ Ejercicio a entregar:  
Se debe desarrollar un pequeño módulo que permita almacenar de forma persistente (archivos) palabras clasificadas por alguna 
categoría. Como por ejemplo separar las palabras por cantidad de sílabas, cantidad de letras, acentuación, idioma, etc. 
Es decir que el módulo va a gestionar una estructura con una o más categorías y dentro de cada una la información en sí. 
Se debe implementar el ABM de categorías (sílabas, cantidad de letras, etc.), el ABM de palabras eligiendo previamente la 
categoría a la cual pertenece. Asimismo se deberán los listados de las categorías, de las palabras por categoría ordenadas 
alfabéticamente. A su vez se requiere que dada una categoría en particular el módulo devuelva aleatoriamente (random) una palabra 
de las que fueron cargadas. 
Nota 1: La entrega se deberá subir obligatoriamente a una tarea creada en “Cátedras”,incluyendo datos ya cargados y un archivo 
README.txt que documente el uso del módulo. Se corregirán únicamente las entregas que allí se encuentren.
Nota 2: Recomendamos la utilización de Pickle para guardar las estructuras completas en el                            
archivo (Ref. https://docs.python.org/3.2/library/pickle.html).

Debido a algunas consultas por parte de ustedes es que mandamos algunas aclaraciones sobre la Entrega 1
 
 
* La carga tanto de categorías como de palabras que se pide es completamente manual
* No hay procesamiento automático de las palabras para categorizarlas, lo que se pide para el alta es que por teclado el usuario 
indique a qué categoría quiere agregar una palabra y luego la palabra en sí, pero la decisión de a qué categoría se asigna cada 
palabra la toma el usuario.
* Todas las palabras y categorías deben guardarse en un único archivo, realizando la persistencia y la recuperación de datos 
mediante Pickle, y utilizando una estructura adecuada para almacenar correctamente la información (categorías y palabras).
* "ABM" hace referencia a "Alta, Baja y Modificación": Crear nuevas categorías/palabras, Borrar categorías/palabras existentes, 
y Modificar categorías/palabras existentes.
 
Ejemplo del alta de una categoría
 
1. El módulo Python le solicita al usuario que indique el nombre de la categoría
2. El usuario escribe la categoría y presiona <ENTER>
3. El módulo valida que la categoría no exista
  3.1. Si la categoría no existe, la da de Alta y la guarda en el archivo
  3.2. Si la categoría sí existe, indica el error y pide al usuario que ingrese una nueva categoría, volviendo al paso 1.
 
Ejemplo del alta de una palabra
 
1. El módulo Python le solicita al usuario que indique a qué categoría desea agregar una palabra
2. El usuario indica la categoría
3. El módulo valida que la categoría exista
  3.1. Si no existe, vuelve al paso 1. con un mensaje de error
  3.2. Si existe, continúa al paso 4.
4. El módulo solicita al usuario que ingrese la nueva palabra.
5. El usuario ingresa la palabra.
6. El módulo valida que la palabra no exista en esa categoría
  6.1. Si la palabra existe, indica el error y vuelve al paso 4.
  6.2. Si la palabra no existe, la da de Alta y guarda en el archivo
 
Saludos
Fecha tope de entrega: Lunes 28/4 a las 10 AM
Fecha de coloquios:  Lunes 28 y Martes 29 en los horarios de práctica


"""

import ABM
import pickle
import random


menuVerArch = (
    "\nMenu\n------------------------------------------------\n\t" + "1:Ver Archivo\n\t2:Ver Categorias\n\t3:Ver palabra por categoria\n\t4:Ver categoria random\n\t5:Ver categoria con palabra random\n\t6:Ver por medio de una categoria dada una palabra random\n\t7:Salir\n\t" + "Ingrese la opcion: ")  # funcion y excepciones
menuBajaArchi = (
    "\nMenu\n------------------------------------------------\n\t" + "1:Borrar Categorias\n\t2:Borrar Palabras\n\t3:Salir\n\t" + "Ingrese la opcion: ")
menuModArch = (
    "\nMenu\n------------------------------------------------\n\t" + "1:Modificar Categorias\n\t2:Modificar Palabras\n\t3:Salir\n\t" + "Ingrese la opcion: ")  # ponerlo en funcion y ver excepciones
menuAlta = (
    "\nMenu\n------------------------------------------------\n\t" + "1:Crear Categorias\n\t2:Crear Palabras\n\t3:Salir\n\t" + "Ingrese la opcion: ")
menuGral = (
    "\nMenu\n------------------------------------------------\n\t" + "1:Crear\n\t2:Borrar\n\t3:Modificar\n\t4:Vertexto\n\t5:Salir\n\t" + "Ingrese la opcion: ")


def imprimir_menu(menu):
    try:
        print(menu)
        op = int(input('Ingrese la opcion: '))
    except:
        print('todo mal')
        return 'errorm'
    else:
        return op


def escriturapickle(diccionario):  # error por oserror
    try:
        archivosal = open('pickle.txt', 'wb')  # Escritura de archivo binaria (wb)
        pickle.dump(diccionario, archivosal)  # Agrego informacion al archivo
        archivosal.close()  # Cierre del archivo
    except (OSError, IOError):
        return 'errorw'


def lecturapickle():
    try:
        archivoent = open('pickle.txt', 'rb')  # Lectura de archivo rb
        nuevodic = pickle.load(archivoent)  #
        archivoent.close()
    except (EOFError):
        return 'errorl'
    else:
        return nuevodic


diccionario = {}  # excepciones de archivo
# opc=excepcionopcion()
opc = imprimir_menu(menuGral)
exito = False
while (opc != 5):
    band = True
    if (opc == 1) and not (opc == 'errorm'):  # Ingresa a la opcion 1 para crear
        opc = imprimir_menu(menuAlta)
        while (opc != 3) and not ( opc == 'errorm'):  # me pregutan que tipo de creado voy hacer 1-crear categorias y 2 crear palabras
            if (opc == 1):  # alta categoria
                categoria = (input(("Ingrese una categoria: "))).lower()  # str.lower() convierte el texto en minuscula
                exito = ABM.Altacategoria(diccionario, categoria, exito)
                while (exito == False):
                    exito == False
                    categoria = (input("Ingrese una categoria: ")).lower()
                    exito = ABM.Altacategoria(diccionario, categoria, exito)
            if (opc == 2):  # alta palabra
                categoria = (input("Ingrese una categoria: ")).lower()# ingresa una categoria y la convierte en minuscula
                palabra = (input("Ingrese una palabra: ")).lower()# ingresa una palabra y la convierte en minuscula
                exito = ABM.Altapalabra(diccionario, categoria, palabra, exito)# cargo el diccionario la categoria donde se encuenta y la palabra para dar de alto, y si se produzco exito
                while (exito == False):
                    categoria = (input("Ingrese una categoria: ")).lower()
                    palabra = (input("Ingrese una palabra: ")).lower()
                    exito = ABM.Altapalabra(diccionario, categoria, palabra, exito)
        if (escriturapickle(diccionario) == 'error'):
            print('Se produjo un error en la estructura del archivo vuelva a crearlo')
            band = False
        if band:
            print(diccionario)
            opc = imprimir_menu(menuAlta)
elif ((opc == 2) and (not (opc == 'errorm'))):  # borrar
    opc = imprimir_menu(menuBajaArchi)
while (opc != 3) and not (opc == 'errorm'):
    if (opc == 1):  # baja categoria
        categoria = (input("Ingrese una categoria: ")).lower()#ingreso una categoria que va ser transformado en minuscula
        exito = ABM.Bajacategoria(diccionario, categoria, exito)
        while (exito == False):
            categoria = (input("Ingrese una categoria: ")).lower()
            exito = ABM.Bajacategoria(diccionario, categoria, exito)
    if (opc == 2):  # baja palabra
        categoria = (input("Ingrese una categoria para buscar una palabra para eliminar: ")).lower()#ingreso una categoria que va ser transformado en minuscula
        palabra = (input("Ingrese una palabra que desee eliminar: ")).lower()#ingreso una palabra que va ser transformado en minuscula
        exito = ABM.Bajapalabra(diccionario, categoria, palabra, exito)
        while (exito == False):
            print("Ingrese categoria o palabra: ")
            categoria = (input("Ingrese una categoria para buscar una palabra para eliminar: ")).lower()
            palabra = (input("Ingrese una palabra que desee eliminar: ")).lower()
            exito = ABM.Bajapalabra(diccionario, categoria, palabra, exito)

    if (escriturapickle(diccionario) == 'error'):
        print('Se produjo un error en la estructura del archivo vuelva a crearlo')
        band = False
    if (band):
        print(diccionario)
        opc = imprimir_menu(menuBajaArchi)

elif (opc == 3) and (not (opc == 'errorm')):  # modificar
opc = imprimir_menu(menuModArch)
while (opc != 3):
    if (opc == 1):  # modificar categoria
        categvieja = (input("Ingrese una categoria que se desee modificar: ")).lower()#Ingresa una categoria a buscar, es convertida en minuscula
        categnueva = (input("Ingrese un nombre para categoria: ")).lower()#Ingresa una categoria amodificar, es convertida en minuscula
        ABM.Modificarcategoria(diccionario, categnueva, categvieja, exito)
        while (exito == False):
            categvieja = (input("Ingrese una categoria que se desee modificar: ")).lower()
            ABM.Modificarcategoria(diccionario, categnueva, categvieja, exito)
    if (opc == 2):  # modificar palabra hacer funciones
        categoria = (input("ingrese una categoria: ")).lower() #Agrego una categoria a buscar
        palvieja = (input("Ingrese una palabra que deseo buscar en dicha categoria: ")).lower()
        palnueva = (input("Ingrese una nueva palabra para modificar: ")).lower()  # agregar excepciones de tipor entero y general
        exito = ABM.Modificarpalabra(diccionario, categoria, palnueva, palvieja, exito)
        while (exito == False):
            categoria = (input("ingrese una categoria: ")).lower()
            palvieja = (input("Ingrese una palabra que deseo buscar en dicha categoria: ")).lower()
            exito = ABM.Modificarpalabra(diccionario, categoria, palnueva, palvieja, exito)

    if (escriturapickle(diccionario) == 'error'):
        print('Se produjo un error en la estructura del archivo vuelva a crearlo')
        band = False
    if (band):
        print(diccionario)
        opc = imprimir_menu(menuModArch)
elif (opc == 4) and (not (opc == 'errorm')):  # ver, y agregar el random
opc = imprimir_menu(menuVerArch)
band = True
while (opc != 7) and (band):
    if (opc == 1):  # ver archivo
        if (lecturapickle() != 'error'):
            print(lecturapickle())  # trabajarlo con /n /t para quede mejor
        else:
            print('Se produjo un error en la lectura del archivo vuelva a crearlo')
            band = False
    elif (opc == 2):  # ver categoria
        if (lecturapickle() != 'error'):
            print(list(lecturapickle().keys()))  # trabajarlo con /n /t para que quede mejor
        else:
            print('Se produjo un error en la lectura del archivo vuelva a crearlo')
            band = False
    elif (opc == 3):  # ver palabras
        if (lecturapickle() != 'error'):
            print(list(lecturapickle().values()))  # trabajarlo con /n /t para que quede mejor
        else:
            print('Se produjo un error en la lectura del archivo vuelva a crearlo')
            band = False
    elif (opc == 4):
        if (lecturapickle() != 'error'):
            print(random.choice(list(lecturapickle().keys())))  # trabajarlo con /n /t para que quede mejor
        else:
            print('Se produjo un error en la lectura del archivo vuelva a crearlo')
            band = False
    elif (opc == 5):
        if (lecturapickle() != 'error'):
            print(random.choice(list(lecturapickle().values())))  # trabajarlo con /n /t para que quede mejor
        else:
            print('Se produjo un error en la lectura del archivo vuelva a crearlo')
            band = False
    elif (opc == 6):
        if (lecturapickle() != 'error'):
            categoria = (input(("Ingrese una categoria: "))).lower()
            lista = (list(lecturapickle()))  # trabajarlo con /n /t para que quede mejor
            print(random.choice(lista[lista.index(categoria)].values()))
        else:
            print('Se produjo un error en la lectura del archivo vuelva a crearlo')
            band = False
    if band:
        opc = imprimir_menu(menuVerArch)
else:
    print("Ingreso una opcion incorrecta")
print("Ingrese una opcion nuevamente: ")
opc = imprimir_menu(menuGral)
print('Programa finalizado')

