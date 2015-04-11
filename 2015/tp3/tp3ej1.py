# -*- coding: utf-8 -*-
__author__ = 'guillermo'

"""Importante: todos los ejercicios debe probarlos tanto en Python 2.x como Python 3.x, salvo que se indique lo
contrario.
La utilización de algunos caracteres de nuestro lenguaje puede generar error unicode, por lo cual es necesario agregar
el comienzo del script:
# -*- coding: utf-8 -*-

Funciones y Módulos
1. Implemente las funciones vistas de operaciones sobre conjuntos (unión, intersección, diferencia simétrica y resta)
que reciban los dos conjuntos y devuelvan el resultante."""

def union(mujeres,hombres):
    return mujeres | hombres


def interseccion(mujeres,hombres):
    return mujeres & hombres

def difsimetrica(mujeres,hombres):
    return mujeres ^ hombres

def resta (mujeres, hombres):
    return mujeres - hombres

mujeres = set(['marta', 'lucrecia', 'norma'])
hombres = set(['jose', 'cristian', 'luis'])

print 'la union entre ambos conjuntos es:', union(mujeres, hombres)
print 'la interseccion entre ambos conjuntos es:', interseccion(mujeres, hombres)
print 'la diferencia simetrica entre ambos conjuntos es:', difsimetrica(mujeres, hombres)
print 'la resta entre ambos conjuntos:', resta(mujeres, hombres)