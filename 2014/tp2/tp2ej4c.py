"""
c) Ahora imprima la suma de los primeros N números impares, siendo N un entero ingresado por la entrada
estándar. Resuelvalo utilizando tanto for..in como while
range(1,10,2)
[1, 3, 5, 7, 9]

"""

num = int(input('ingrese la cantidad de numero impares que deseo sumar: '))
sumar = 0
for x in range(0, num + 1):
    if x % 2 == 1:
        sumar += x
print('la suma de los ' + str(num) + ' es = ' + str(sumar))

cant = int(input('ingrese la cantidad de numero impares que deseo sumar: '))
num = 1
sumar = 0
while num <= cant:
    if num % 2 == 1:
        sumar = sumar + num
    num += 1
print(sumar)
