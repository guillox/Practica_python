"""
	Módulos
8.- Escriba cada uno de los incisos del ejercicio 7.- (a, b y c) en módulos diferentes (conjuntos.py, cola.py,
parametros_variables.py), impórtelos en un nuevo módulo (principal.py) y utilice sus funciones en éste último.
conjuntos.py
"""

def union(conjunto1,conjunto2):
	return conjunto1|conjunto2

def interseccion(conjunto1,conjunto2):
	return conjunto1 & conjunto2

def diferencia(conjunto1,conjunto2):
	return conjunto1 - conjunto2			


conjunto1 = set([1,2,3,4,5,6])
conjunto2 = set([3,4,5,10,15])
print (union(conjunto1,conjunto2))
print (interseccion(conjunto1,conjunto2))
print (diferencia(conjunto1,conjunto2))