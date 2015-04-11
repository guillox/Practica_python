# coding=utf-8
__author__ = 'guillermo'
"""14. Ingresar el CUIL de una persona e imprimir su número de documento."""

cuil = raw_input('Ingrese su numero de cuit:')
print 'Su numero de documento es:', cuil.split('-')[1]
