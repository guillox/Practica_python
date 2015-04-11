__author__ = 'guillermo'

lista = [2, 3, 2.3, [1, 'a'], 'a', 'true', 3]
print(lista)  # 1- imprimo la lista completa
print(lista[0])  # 2- imprimo el primer elemento de la lista
print(lista[-1])  # 3- imprimo el ultimo elememnto de la lista
print(lista[2:])  # 4- imprimo del segundo elemento hasta el final de la lista
print(lista[:3])  # 5- imprimo del el primer elemento hasta la posicion 3-1
print(lista[:])  # 6- imprime todos los elementos de la lista
print(lista[0:-1])  # 7- imprimo el primer elemento
print(lista[3][1])  # 8- imprimo el tercer elemento de la lista y el elemento 1 de la sub lista
print(lista[3][:])  # 9- imprimo el tercer elemento de la lista y todos los elementos de la sublista
print(len(lista[3]))  # 10- imprimo el tamaño de la sublista de la lista
print(len(lista))  # 11- imprime tamaño de la lista
listan = [1, 2, 5, 2, 2.6, 25, -1, 0,-23,-50]
print(max(listan))  # 12- imprime el max de la listan
print(min(listan))  # 13- imprime el min de la listan
print(sum(listan))  # 14- imprime la suma de los elementos de la listan
print(all(
    listan))  # 15- Devuelve True si todos(all) los elemento de listan son True, si sos numero <>0 se considerean true
print(any(listan))  # 16- Devuelve True si alguno(any) de los valores en L es True
print(lista.reverse())  # 17- imprime alreves la lista
print(lista[0])  # 18
print(lista[-1])  # 18
print(lista)  # 19
print(lista.reverse())  # 20- vuelvo a invertir la lista
print(lista[0:3])  # 21 imprime la lista de la posicion 0 hasta 3-1
print(lista.count(3))  # 22 imprime la cantidad de veces que aparece el 3 en la lista
print(lista[3].count(1))  # 23 imprime la cantidad de veces que aparece el 1 en la sublista
print(lista.index(3))  # 24 imprime el indice o la posicion del elemento a en la lista
print(lista.index([1, 'a']))  # 25 imprime el indice o la posicion del elemento lista en la lista
print(lista[3].index('a'))  # 26 imprime el indice del elemento a en el sublista
print(lista.index(2, 0, 4))  # 27 imprime el indice o la posicion del elemento 3 en la lista entre la posicion 0 y 2

#ordenar lista
listac=['a','j','t','Q','1','z','A','ab','@','9']
listan.sort()
print(listan)
listac.sort()
print(listac)

# agregar elemento
elemento = input('ingrese un elemento')
lista.append(elemento)  # agrega un elemento al final de la lista
print(lista)  #
print(lista[3].append(1))  # agrega un elemento al final del sublista
print(lista + [1, 2, 3])  # agrego al finallos elementos 1,2,3 en la lista
print(lista * 2)  # imprimo la lista 2 veces
print(lista[3] + [3, 4, 5])  # concateno en la posicion 3 de la lista, sublista agregando al final l 3,4,5
print(lista[3] * 2)  # repito el 2 veces el contenido de la posicion 3 sublista
print(lista + [{2:3}])
lista.insert(3,'abv')# inserto en la posicion 3 el elemento abv y desplazo todo uno a la derecha permitiendo que el ultimo desaparezca
print(lista)
lista.insert(9,1)# puedo insertar en la ultima posicion el elemento 1 y no se hacce desplazamiento
print(lista)
lista[4].insert(0,23)# inserto el elemento 23 en la posicion 4 de la lista y sublista pos 0
print(lista)
lista[4].insert(4,1)# inserto el elemento 1 en la posicion 4 de la lista y sublista pos 4
print(lista)
lista[4].insert(10,-1)# inserto el elemento -1 en la posicion 4 de la lista y sublista pos 10 que lo toma como al final de la sublista
print(lista)

elemento = input('ingrese un elemento')
lista.extend(elemento)  # agrega un elemento al final de la lista pero como lista
print(lista)
lista.extend({2: 4})
print(lista)

#recorrido
for i in lista:# donde i son todos los elementos de lista
    print (i)
    if i % 2==0:
for i in range(len(lista)):
    if lista[i]==1:
        lista.append(1)
    else:


# eliminar
lista.remove(2)  # remueve la primer ocurrencia de 2
print(lista)


lista2 = lista.copy()
lista3 = lista
print(lista2)
print(lista3)
lista.clear()  # borra todos los elementos de la lista
print(lista)   # borra todos los elementos de la lista, es borrado
print(lista2) # en ete caso no se borra la lista 2 ya q le pase por copia a lista
print(lista3)   # en este caso se borra lista 3 ya q le pase lista por asignacion
del lista2[1]
print(lista2)
