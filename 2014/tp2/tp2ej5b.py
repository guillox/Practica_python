"""
5.- a) Dada una lista con N números, modifique dicha lista multiplicando por 2 cada uno de los elementos. Es
decir, si tengo [2, 3, 4, 5, 6] el resultado sería [4, 6, 8, 10, 12].
b) Modifique el ejercicio anterior para que a los números impares los eleve al cuadrado y a los pares al cubo.
range(0, len(lista))
"""
lista = [2, 3, 4, 5, 6]
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        lista[i] **= 2
    else:
        lista[i] **= 3
print(lista)























