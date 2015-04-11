# coding=utf-8
__author__ = 'guillermo'

"""12. Dada una dirección de mail ingresada por teclado, imprima el nombre de usuario y el
nombre del servidor."""

direccion = raw_input('ingrese una direcion completa de correo:')
print 'el nombre de usuario es:', direccion.split('@')[0]
print 'el nombre del servidor es:', direccion.split('@')[1]


