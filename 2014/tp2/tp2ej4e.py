"""
e) Modifique d) para que si en algún momento determinado la suma de los números impares da mayor que
50 corte la ejecución del bucle. Nuevamente resuélvalo utilizando while y for..in.

"""

num = int(input('ingrese la cantidad de numero impares que deseo sumar: '))
sumar = 0
for x in range(5, num + 1):
    if x % 2 == 1:
        sumar += x
    if sumar > 50:
        break  # sale del for cuando la suma es mayor a 50

print('la suma de los ' + str(num) + ' es = ' + str(sumar))

cant = int(input('ingrese la cantidad de numero impares que deseo sumar: '))
num = 5
sumar = 0
while (num <= cant) and (sumar <= 50):
    if num % 2 == 1:
        sumar = sumar + num
    num += 1
print(sumar)
