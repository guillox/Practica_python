# coding=utf-8
__author__ = 'guillermo'
"""17. Ingresar la compra de 3 productos diferentes con sus precios unitarios y
cantidades e imprimir el total de cada producto y la suma total gastada."""

prec1 = int(raw_input('ingrese el precio del producto 1:'))
cant1 = int(raw_input('ingrese la cantidad de producto 1:'))
prec2 = int(raw_input('ingrese el precio del producto 2:'))
cant2 = int(raw_input('ingrese la cantidad de producto 2:'))
prec3 = int(raw_input('ingrese el precio del producto 3:'))
cant3 = int(raw_input('ingrese la cantidad de producto 3:'))
print 'el total del producto 1 es:', prec1*cant1, ';el total del producto 2 es:', prec2*cant2, ';el total del producto 3 es:', prec3*cant3
print 'la suma total gastada:', (prec1*cant1+prec2*cant2+prec3*cant3)