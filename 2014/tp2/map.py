__author__ = 'guillermo'

# archivo con funcion lambda(anonima)

cuadrado = lambda x: x * 2
lista = [2, 3, 4, 5, 6]
for i in range(0, len(lista)):
    lista[i] = cuadrado(lista[i])

print(lista)

# archivo con funcion map(sin for) map(f(x),[x])
lista = [2, 3, 4, 5, 6]

print(list(map(lambda a: a * 2, lista)))

#archivo con funcion filter (retorna el resultado de la funcion si esta es verdadera
lista = [2, 3, 4, 5, 6]
print(list(filter(lambda a: a < 2, lista)))


#comun
lista2 = [1, 2, 3, 4, 5, 6]
for i in range(0, len(lista2)):
    if lista2[i] % 2 == 0:
        lista2[i] *= 2
    else:
        lista2[i] *= 3
print(lista2)

#con funcion lambda

lista2 = [1, 2, 3, 4, 5, 6]
cua = lambda x: x ** 2
cub = lambda x: x ** 3

for i in range(0, len(lista2)):
    if lista2[i] % 2 == 0:
        lista2[i] = cua(lista2[i])
    else:
        lista2[i] = cub(lista2[i])
print(lista2)

#funcionn map sin for, es iterativo

lista2 = [1, 2, 3, 4, 5, 6]
print(list(map()))


