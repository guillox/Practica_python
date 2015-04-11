"""

2.- a) Explique la semántica de los bucles while y for..in. Transcriba los ejemplos vistos en teoría en un módulo Python
y ejecútelos.

"""
# imprime los primeros 20 numero pares
num = 0
while (num < 20):
    if num % 2 == 0:
        print(str(num) + "es uno de los primeros numeros pares")
    num += 1  # igual que num=num+1

# recorrido de la lista
lista = ["el", "for", "ha", "recorrido", "toda", "la", "lista"]
for elmento in lista:
    print(elmento)





#recorre la lista imprimiendo con el numero del elemento
lista = ["el", "for", "usado", "como", "otros", "lenguajes"]
for elemento in range(6):
    print("Elemento ", elemento, " de la lista es:", lista[elemento])


#imprime los numeros primos que hay entre 
n = 1

for n in range(2, 10):
    band = True
    for x in range(2, n):
        if n % x == 0:
            print(n, 'no es un numero primo', x)
            band = False
            break
    if band:
        print(n, 'Es un numero primo')

#recorrido 2
b = 1
lista2 = [1, 2, '2', 'a', [1, 2], b]
for elemento1 in lista2:
    if lista2[elemento1] == 2:
        print('el elemento fue encontrado')
print(lista2[0])#imprime el primer elemento
print(lista2[0:2])#imprime desde el primer hasta el 2do -1
print(lista2[0:5:2])#imprime del primer elemento hasta el 5to-1 de salto de 2
print(lista2[-1])#imprime el ultimo elemento
print(lista2[-1:-3])#imprime el ultimo hasta el -4
