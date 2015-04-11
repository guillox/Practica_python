

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
