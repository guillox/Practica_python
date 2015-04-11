"""
Listas, Tuplas y Diccionarios
12.- Listas
Dada la siguiente lista:
lista = [ 'elemento1' , 2 ,   'elemento 3',   'elemento 4' ]

g) ¿Qué sucede si ejecutamos el siguiente código? ¿Por qué? ¿Qué debería hacer para                          
agregar un nuevo elemento al final de la lista?
lista[4]   = 'elemento 5' 
me tira un error pq el indice esta fuera de rango en la lista 
"""

lista = [ 'elemento1' , 2 ,'elemento 3', 'elemento 4' ]
lista.append('elemento 5')
print lista[:]


