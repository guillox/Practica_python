""" 7.- a) Implemente las funciones vistas de operaciones sobre conjuntos (unión, 
intersección y diferencia) de manera tal que cada una reciba los dos conjuntos y 
devuelva el resultante.
conjunto1= set([1, 2, 3, 4, 5, 6])
conjunto2 = set([3, 4, 5, 10, 15]) """



def union(conjunto1,conjunto2):
	print conjunto1|conjunto2

def interseccion(conjunto1,conjunto2):
	print conjunto1&conjunto2

def diferencia(conjunto1,conjunto2):
	print conjunto1-conjunto2

conjunto1= set([1, 2, 3, 4, 5, 6])
conjunto2 = set([3, 4, 5, 10, 15])
union(conjunto1, conjunto2)
interseccion(conjunto1,conjunto2)
diferencia(conjunto1, conjunto2)
