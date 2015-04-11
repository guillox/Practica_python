# coding=utf-8
__author__ = 'guillermo'
"""20. Dada la siguiente lista
lista = ['Juan', 40, 'raqueta', True, -10.5, None ]
a. Imprima por separado su longitud, su primer y último elemento
b. Imprima los dos últimos elementos (sin utilizar su longitud)
c. Modifíquela para reemplazar en una sola línea el segundo y tercer elemento por 25
y 'pelota' respectivamente. ¿Qué pasa si agregamos más elementos que posiciones?
d. ¿Qué sucede si hacemos lista[len(lista)] = False? Escriba dos maneras de agregar el
elemento False al final de la lista
e. Elimine el segundo elemento de la lista. ¿Cómo haría para eliminar los tres últimos
elementos en una sola instrucción?
f. Sean lista1 la lista que venimos utilizando y lista2 = [9, 'Claudia'], escriba dos formas
de agregar lista2 al final de lista1.
g. Imprima la lista al revés pero sin modificar la lista original"""


lista = ['Juan', 40, 'raqueta', True, -10.5, None]

#a. Imprima por separado su longitud, su primer y último elemento
print 'la longitud de la lista es:', len(lista)
print 'el primer elemento de la lista es:', lista[0]
print 'el ultimo elemento de la lista es:', lista[-1]

#b. Imprima los dos últimos elementos (sin utilizar su longitud)
print 'Muestro los dos ultimos elementos de la lista:', lista[-1], ',', lista[-2]

"""c. Modifíquela para reemplazar en una sola línea el segundo y tercer elemento por 25 y 'pelota' respectivamente. ¿Qué pasa si agregamos más elementos que
posiciones?
se agregaria en la siguiente posicion agrandando la lista
lista[1:2] = [25, 'pelota', 34]
print lista
>>> ['Juan', 25, 'pelota', 34, 'raqueta', True, -10.5, None]

"""
lista[1:2] = [25, 'pelota']
print lista

"""d. ¿Qué sucede si hacemos lista[len(lista)] = False? Escriba dos maneras de agregar el elemento False al final de la lista
Se me queda fuera de rango por eso no lo puedo ingresar

lista[len(lista)] = False
print lista
"""
lista.append(False)
print lista

#e. Elimine el segundo elemento de la lista. ¿Cómo haría para eliminar los tres últimos elementos en una sola instrucción?

del lista[1]
print lista

del lista[-3:len(lista)]
print lista

#f. Sean lista1 la lista que venimos utilizando y lista2 = [9, 'Claudia'], escriba dos formas de agregar lista2 al final de lista1.

#forma 1
lista2 = [9, 'Claudia']
print lista + lista2

#forma 2
lista.append(lista2)
print lista

#g. Imprima la lista al revés pero sin modificar la lista original
lista3 = lista[:]
lista3.reverse()
print lista3
print lista

