"""12.-  Listas
Dada la siguiente lista
lista= ['elemento1', 2, 'elemento3', 'elemento4']

g) Que sucede si ejecutamos el siguiente codigo Por que Que deberia hacer para agregar un nuevo elemento al 
final de la lista
lista[4]='elemento5'
"""
lista= ['elemento1', 2, 'elemento3', 'elemento4']
lista.append('elemento5')
print lista 

#otra forma
lista.insert(3,'elemento5')
print lista
