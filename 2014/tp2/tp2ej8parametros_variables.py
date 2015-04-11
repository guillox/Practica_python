"""
Módulos
8.- Escriba cada uno de los incisos del ejercicio 7.- (a, b y c) en módulos diferentes (conjuntos.py, cola.py,
parametros_variables.py), impórtelos en un nuevo módulo (principal.py) y utilice sus funciones en éste último.
parametros-variables.py
"""

def funcd(lista,diccionario):
	for elemento in lista:
		if elemento in diccionario.keys():
			print elemento


lista=[2,4,6,7,8]
diccionario = {1: 'pedro', 2: 'oscar',3:'pepe'}
funcd(lista,diccionario)