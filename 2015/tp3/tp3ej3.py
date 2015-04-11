
# -*- coding: utf-8 -*-
__author__ = 'guillermo'
"""3. Implemente la función está(): que reciba una lista variable de números y un diccionario.
Por cada uno de ellos tiene que imprimir si está o no ese número como clave en el diccionario"""

def esta(diccionario, *param):
    for i in range(0, len(param)):
        if diccionario.has_key(param[i]):
            print param[i]


diccionario = {1: 'carlos', 2: 'Rodrigo', 3: 'Jose', 4: 'Guillermo', 9: 'Nicolas', 11: 'Emanuel'}
esta(diccionario, 1, 5, 8, 9, 3, 10)