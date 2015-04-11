# coding=utf-8
__author__ = 'guillermo'

"""13. Ingresar tres palabras desde teclado separadas por un espacio e imprimir sus iniciales y
la cantidad de letras de cada una. ( Ayuda : puede utilizar la función split)

split(' ')
len()
count()

"""

palabras = raw_input('Ingrese tres palabras separadas por espacio:')
print 'Inicial de la primer palabra:', palabras.split(' ')[0][0], 'cantidad de letras de la primera palabra', len(
    palabras.split(' ')[0])
print 'Inicial de la segunda palabra:', palabras.split(' ')[1][0], 'cantidad de letras de la segunda palabra', len(
    palabras.split(' ')[1])
print 'Inicial de la tercera palabra:', palabras.split(' ')[2][0], 'cantidad de letras de la tercera palabra', len(
    palabras.split(' ')[2])
