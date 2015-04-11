# coding=utf-8
__author__ = 'guillermo'

"""10. Escriba un breve script que lea de teclado una frase y una palabra y responda si la
palabra se encuentra dentro de la frase.

>>> cadena = "bienvenido a mi aplicación".capitalize()
>>> print cadena.find("mi")
13
>>> print cadena.find("mi", 0, 10)
-1


"""
frase = raw_input('ingrese una frase:')
palabra = raw_input('ingrese una palabra:')
if frase.find(palabra) != -1:
    print palabra.find(palabra)
else:
    print('no se encontro la frase')
