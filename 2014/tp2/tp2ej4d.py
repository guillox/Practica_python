"""
d) Modifique c) para que además del número N, se obtenga a partir de qué número se quiere empezar a
buscar los impares, es decir si N = 10 y base = 5 buscaremos los 10 primeros números impares a
partir del 5 y retornaremos la suma de ellos. Elija el bucle que crea más conveniente.
Nota: Controle que N >= 0. El programa no debe continuar mientras N no cumple esa condición (utilizar
bucle).
c) Ahora imprima la suma de los primeros N números impares, siendo N un entero ingresado por la entrada
estándar. Resuelvalo utilizando tanto for..in como while

"""

num = int(input('ingrese la cantidad de numero impares que deseo sumar: '))
sumar = 0
for x in range(5, num + 1):
    if x % 2 == 1:
        sumar += x
print('la suma de los ' + str(num) + ' es = ' + str(sumar))

cant = int(input('ingrese la cantidad de numero impares que deseo sumar: '))
num = 5
sumar = 0
while num <= cant:
    if num % 2 == 1:
        sumar = sumar + num
    num += 1
print(sumar)
