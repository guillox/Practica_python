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



"""


def Altacategoria(diccionario, categoria, exito):
    if (categoria in diccionario.keys()):  # busca si una categoria esta dentro de las claves del diccionario
        print("ingrese una nueva categoria que no se encuentre en el diccionario")
        exito = False
    else:
        diccionario[categoria] = []  # crea una nueva categoria
        exito = True
    return exito


def Altapalabra(diccionario, categoria, palabra, exito):
    if (categoria in diccionario):  # Busca la categoria donde queremos dar de alta la palabra
        if not (palabra in diccionario[categoria]):  # busco si la palabras que voy a dar de alta se encuenta en dicha categoria
            diccionario[categoria].append(palabra)#agrega al final de la lista la palabra lista.append()
            diccionario[categoria].sort()#ordena la palabra dentro de la categoria list.sort([func])
            exito = True

        else:
            print("ingrese una nueva palabra ya que se encuentra en la lista")
            exito = False
    else:
        print("ingrese una nueva categoria ya que no se encuentra en el diccionario")
        exito = False
    return (exito)


def Bajacategoria(diccionario, categoria, exito):
    if (categoria in diccionario):
        del diccionario[categoria]#Da de baja la categoria completa
        exito = True

    else:
        print("ingrese una nueva categoria ya que no se encuentra en el diccionario")
        exito = False
    return exito


def Bajapalabra(diccionario, categoria, palabra, exito):#elimina la palabra de la categoria
    if (categoria in diccionario):# si la categoria esta dentro del las claves del diccionario
        if (palabra in diccionario[categoria]):# si la palabra esta dentro de los valores del diccionario(lista)
            diccionario[categoria].remove(palabra)# elimino la palabra de la lista( diccionario[categoria])
            exito = True
        else:
            print("Ingrese una palabra para que se encuentre en la lista y sea eliminada")
            exito = False
    else:
        print("ingrese una nueva categoria ya que no se encuentra en el diccionario")
        exito = False
    return exito


def Modificarcategoria(diccionario, categnueva, categvieja, exito):# modifico categoria
    if (categvieja in diccionario):#si la categoria se encuenta en el diccionario
        lista = diccionario[categvieja]# guardo la lista de la categoria a modificar
        del diccionario[categvieja]#elimino la categoria
        diccionario[categnueva] = lista# creo una nueva categoria pero con los mismos valores q la anterior categoria
        exito = True
    else:
        exito = False
    return exito


def Modificarpalabra(diccionario, categoria, palnueva, palvieja, exito):
    if (categoria in diccionario):#si la categoria se encuenta en el diccionario
        if (palvieja in diccionario[categoria]):# si la palabra que deseo buscar se encuentra en la lista de dicha categoria
            i = diccionario[categoria].index(palvieja)# obtengo el indice(index) de donde se encuentra la palabra en la lista
            diccionario[categoria][i] = palnueva# Sobre escribo la palabra nueva en la ubicacion encontrada
            exito = True
        else:
            exito = False
            print("Ingrese una palabra que se encuentre en la lista de palabras de la categoria")
    else:
        exito = False
        print("Ingrese nuevamente una categoria que se encuentre en el diccionario para realizar la Modificación")
    return exito
