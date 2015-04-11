"""
5.- a) Dada una lista con N números, modifique dicha lista multiplicando por 2 cada uno de los elementos. Es
decir, si tengo [2, 3, 4, 5, 6] el resultado sería [4, 6, 8, 10, 12].
c) Modifique el código anterior para que los números sean cargados por la entrada estándar hasta recibir el
-100.

otra forma
if num % 2 == 0:
    lista.append(num ** 2)
else:
    lista.append(num ** 3)
"""

num = int(input('ingrese por un numero para ser cargado a la lista '))
lista = []
while num != -100:
    if num % 2 == 0:
        num **= 2  # es igual a poner num =num **2
    else:
        num **= 3  # es igual a poner num =num **3
    lista.append(num)
    num = int(input("ingrese por un numero para ser cargado a la lista "))
print(lista)





















