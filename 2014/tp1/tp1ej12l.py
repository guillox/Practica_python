"""
Listas, Tuplas y Diccionarios
12.- Listas
Dada la siguiente lista:
lista = [ 'elemento1' , 2 ,   'elemento 3',   'elemento 4' ]

l) Cree un string que contenga al menos cinco palabras, sepárelas y ordénelas                        
alfabéticamente y en orden inverso. Imprima cada resultado y la cantidad de palabras del string.                            
Por ejemplo, utilizar la siguiente frase como string: “Python es un lenguaje multiplataforma y de                            
tipado dinamico”.

ejemplo
>>> nombres = "Carlos|Cristina|Rodrigo|Hugo"
>>> nombres.split("|")
["Carlos", "Cristina", "Rodrigo", "Hugo"]

La función sort, nos permite ordenar los elementos de una lista.

l1 = [3, 5, 1, 3, 4]
>>> l1.sort()
>>> l1
[1, 3, 3, 4, 5]

cantidad de elementos len()
>>> l1 = [1, 3, 5]
>>> l2 = ['a', 'b', l1, 'c']
>>> len(l2)
4

"""

lista = "python es un lenguaje multiplataforma y de tipado dinamico"
lista=lista.split(" ")
print type (lista)
print lista[:]
print len(lista)
print sorted(lista)
print len(lista)