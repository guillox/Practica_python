"""
Listas, Tuplas y Diccionarios
12.- Listas
Dada la siguiente lista:
lista = [ 'elemento1' , 2 ,   'elemento 3',   'elemento 4' ]
i) ¿Cómo puedo hacer para retornar el valor del último elemento y eliminarlo de la lista                              
en una sola instrucción?
"""
lista = [ 'elemento1' , 2 ,'elemento 3', 'elemento 4' ]
lista.append(lista.remove('elemento 5'))
print lista[:]

