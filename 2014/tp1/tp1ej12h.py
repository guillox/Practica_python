"""
Listas, Tuplas y Diccionarios
12.- Listas
Dada la siguiente lista:
lista = [ 'elemento1' , 2 ,   'elemento 3',   'elemento 4' ]
h) Elimine el elemento creado en g)
"""
lista = [ 'elemento1' , 2 ,'elemento 3', 'elemento 4' ]
lista.append('elemento 5')
print lista[:]
lista.pop()
print lista[:]
#otra forma
lista.remove("elemento5")
