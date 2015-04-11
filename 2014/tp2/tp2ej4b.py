"""b) Modificar las sentencias de a) para que informe dentro del rango del 2 al 30 (inclusive) qué números son pares y
 cuáles impares.

for i in range(1, 10):
	print (i)
else:
	print ('Termino el bucle')


"""

for i in range(2, 30):
    if i % 2 == 0:
        print(i, 'Es un numero par')
    else:
        print(i, 'Es un numero impar')