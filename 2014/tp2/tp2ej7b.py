"""
b) Desarrolle mediante funciones y listas el funcionamiento de las colas FIFO (el primero en entrar es el primero en salir)
con sus operaciones pop(desapilar), push(apilar) y length recibiendo la lista como parámetro. En la función push si no se envía 
como parámetro ningún elemento por defecto el valor será 0 (cero)

lista.pop() 
list.pop(obj=list[-1])

ejemplo
aList = [123, 'xyz', 'zara', 'abc'];

print "A List : ", aList.pop();
print "B List : ", aList.pop(2);

A List :  abc
B List :  zara



"""

"""def fcolapush(listapush, dato):

    return listapush.append(dato)


def fcolapop(listapop, lista):
    for i in range(1,len(lista)):
        listapop = lista.pop(i)
    return listapop"""

lista = [22, 'casa', "una lista", [1, 2]]
lista2 = []
num = lista.pop()
del lista
print(lista)

"""del lista
lista2.append(lista.pop())
del lista
print(lista2)"""
"""listapush = []
listapop = []
for i in range(1, len(lista)):
    dato = lista[i]
    fcolapush(listapush, dato)
fcolapop(listapop, lista)"""


