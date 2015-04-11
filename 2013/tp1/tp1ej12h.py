"""12.-  Listas
Dada la siguiente lista
lista= ['elemento1', 2, 'elemento3', 'elemento4']
h) Elimine el elemento creado en g
"""
lista= ['elemento1', 2, 'elemento3', 'elemento4']
# se puede hacer con dos funciones del() y remove()
#remove() Igual que en la busqueda, elimina la primera aparicion del elemento y si no lo encuentra nos lanzara una excepcion.
lista.append('elemento5')
lista.remove('elemento5')
print lista 

#del() podemos borrar un elemento por su indice
lista.append('elemento5')
del lista[4]
print lista 

