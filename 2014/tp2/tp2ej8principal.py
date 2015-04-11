"""
Módulos
8.- Escriba cada uno de los incisos del ejercicio 7.- (a, b y c) en módulos diferentes (conjuntos.py, cola.py,
parametros_variables.py), impórtelos en un nuevo módulo (principal.py) y utilice sus funciones en éste último.

principal.py

3 formas de importar
1- import tp2ej8conjuntos
   tp2ej8conjuntos.union

2- from tp2ej8conjuntos import union
   fron tp2ej8conjuntos import union,diferencia

   union(conjuntos1,conjuntos2)

3 from tp2ej8conjuntos import *(importa todos los metodos del archivo.py)

cases = ['zero()','one()','two()','three()']

def zero():
  print "method for 0 called..."
def one():
  print "method for 1 called..."
def two():
  print "method for 2 called..."
def three():
  print "method for 3 called..." 
i = int(raw_input("Enter choice between 0-3 "))
if(i<=len(cases)):
 exec(cases[i])
else:
 print "wrong choice"

"""
import tp2ej8conjuntos
import tp2ej8cola
import tp2ej8parametros_variables

car = str(imput('ingrese una opcion que desea elegir'))

if car == 'a':
    car = str(imput('ingrese una opcion que desea elegir'))
    conjuntos1 = [1, 2, 3, 4]
    conjuntos2 = [5, 6, 7, 8]
    if car == 'a':
        print(tp2ej8conjuntos.union(conjunto1, conjunto2))
if car == 'b':
    print(tp2ej8conjuntos.diferencia(conjunto1, conjunto2))
else:
    print(tp2ej8conjuntos.interseccion(conjunto1, conjunto2))

elif car == 'b':
lista = ['a', 1, 2, 3]
car = str(imput('ingrese una opcion que desea elegir'))
lista = []
if (car='a'):
    listapush = []
    print(tp2ej8cola.fcolapush(lista, listapush))
else:
    listapop = []
    print(tp2ej8cola.fcolapop(lista, listapop))

elif car == 'c':
lista = [2, 4, 6, 7, 8]
diccionario = {1: 'pedro', 2: 'oscar', 3: 'pepe'}
tp2ej8parametros_variables.funcd(lista, diccionario)



