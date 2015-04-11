# coding=utf-8
__author__ = 'guillermo'
"""11. Extienda el ejercicio anterior para que lea un párrafo y cuente cuántas oraciones tiene."""

frase = raw_input('ingrese una frase:')
palabra = raw_input('ingrese una palabra:')
if frase.find(palabra) != -1:
    print frase.find(palabra)
else:
    print('no se encontro la frase')
print frase.count('.')