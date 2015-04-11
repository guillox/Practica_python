"""
Funciones lambda, map y filter
9.- Resuelva los incisos del ejercicio 5 con la combinación de estas funciones.

5.- 
a) Dada una lista con N números, modifique dicha lista multiplicando por 2 cada uno de los elementos. Es decir, si tengo 
[2, 3, 4, 5, 6] el resultado sería [4, 6, 8, 10, 12].
b) Modifique el ejercicio anterior para que a los números impares los eleve al cuadrado y a los pares al cubo.
c) Modifique el código anterior para que los números sean cargados por la entrada estándar hasta recibir el -100.

Expresiones lambda 
Pequeñas funciones anónimas pueden ser creadas con la palabra reservada lambda. Esta función retorna la suma de sus
dos argumentos: lambda a, b: a + b. Las funciones lambda pueden ser usadas objetos de tipo función son requeridos.
Están sintácticamente restringidas a una sola expresión. Semánticamente, son solo azucar sintáctica para definiciones
normales de funciones. Al igual que las funciones anidadas, las funciones lambda pueden hacer referencia a variables
desde el ámbito que la contiene:
 def hacer_incrementador(n):
...   return lambda x: x + n
...
f = hacer_incrementador(42)
f(0)
42
f(1)
43

Lambda nos sirve para crear pequeñas funciones anónimas, de una sola línea sobre la marcha. Las formas lambda se pueden usar en 
cualquier lugar siempre que se necesite un objeto función.


cuadrado = lambda x: x**2
cuadrado(2)
4
 cuadrado(3)
9


función map
map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are 
passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables
, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into 
argument tuples, see

sintaxis 
map(function, iterable, ...) python 2.7
map(function, iterable, ...) python 3.4

Ejemplos:
map(lambda a: a+1, [1,2,3,4])
[2, 3, 4, 5]
map(lambda a, b: a+b, [1,2,3,4], (2,3,4,5))
[3, 5, 7, 9]
map(lambda a, b: a + b if b else a + 10, [1,2,3,4,5], (2,3,4,5))   ＃ the second iterable list is one item short
[3, 5, 7, 9, 15]
map(None, [1,2,3,4,5], [1,2,3])
[(1, 1), (2, 2), (3, 3), (4, None), (5, None)]


funcion filter
Namespace:  Python builtin
Docstring:
filter(function or None, sequence) -> list, tuple, or string

Return those items of sequence for which function(item) is true.  If
function is None, return the items that are true.  If sequence is a tuple
or string, return the same type, else return a list.

sintaxis 
filter(function, iterable) python 3.4
filter(function, iterable) python 2.7

Ejemplo:
filter(lambda d: d != 'a', 'abcd')  #filter out letter 'a'。
	'bcd'
def d(x):　＃ not using lambda function, instead using a predefined function
    return True if x != 'a' else False
filter(d, 'abcd')
	'bcd'



"""
# archivo comun
lista = [2, 3, 4, 5, 6]
for i in range(0, len(lista)):
    lista[i] = lista[i] * 2

print(lista)

#archivo con funcion lambda

cuadrado = lambda x: x * 2
lista = [2, 3, 4, 5, 6]
for i in range(0, len(lista)):
    lista[i] = cuadrado(lista[i])

print(lista)

#archivo con funcion map(sin for) map(f(x),[x])
lista = [2, 3, 4, 5, 6]

print(list(map(lambda a: a * 2, lista)))

#archivo con funcion filter
lista = [2, 3, 4, 5, 6]
print(list(filter(lambda a: a * 2, lista)))




#archivo comun
lista = [2, 3, 4, 5, 6]
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = lista[i] ** 2
    else:
        lista[i] = lista[i] ** 3
print(lista)

#archivo con funcion lambda
cuadrado = lambda x: x ** 2
cubo = lambda x: x ** 3

lista = [2, 3, 4, 5, 6]
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = cuadrado(lista[i])
    else:
        lista[i] = cubo(lista[i])
print(lista)

#archivo con funcion map	
"""Ejemplos:
>>> map(lambda a: a+1, [1,2,3,4])
[2, 3, 4, 5]
>>> map(lambda a, b: a+b, [1,2,3,4], (2,3,4,5))
[3, 5, 7, 9]
>>> map(lambda a, b: a + b if b else a + 10, [1,2,3,4,5], (2,3,4,5))   ＃ the second iterable list is one item short
[3, 5, 7, 9, 15]
>>> map(None, [1,2,3,4,5], [1,2,3])
[(1, 1), (2, 2), (3, 3), (4, None), (5, None)]"""


def parimpar(n):
    if n % 2 == 0:
        n = n ** 2
    else:
        n = n ** 3
    return n;


lista = [2, 3, 4, 5, 6]
print(list(map(parimpar, lista)))


#archivo con funcion filter

def parimpar(n):
    if n % 2 == 0:
        n = n ** 2
    else:
        n = n ** 3
    return n;


lista = [2, 3, 4, 5, 6]
print(list(filter(parimpar, lista)))





#archivo comun
num = input('ingrese por un numero para ser cargado a la lista ')
lista = []
while num != -100:
    if num % 2 == 0:
        num = num ** 2
    else:
        num = num ** 3
    lista.append(num)
    num = (input('ingrese por un numero para ser cargado a la lista '))
print(lista)


#archivo con funcion lambda
cuadrado = lambda x: x ** 2
cubo = lambda x: x ** 3
modulo = lambda x: x % 2
num = input('ingrese por un numero para ser cargado a la lista ')
lista = []
while num != -100:
    if modulo == 0:
        num = cuadrado(num)
    else:
        num = cubo(num)
    lista.append(num)
    num = input('ingrese por un numero para ser cargado a la lista ')
print(lista)

# archivo con funcion map
num = input('ingrese por un numero para ser cargado a la lista ')
lista = []
while num != -100:
    if num % 2 == 0:
        num = num ** 2
    else:
        num = num ** 3
    lista.append(num)
    num = input('ingrese por un numero para ser cargado a la lista ')
print(lista)

print(list(map(funcion, lista)))


#archivo con funcion filter


