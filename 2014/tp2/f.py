
def funcd(*lista,diccionario):
	for elemento in lista:
		if lista[elemento] in diccionario:
			print (lista[elemento])


lista=[2,4,6,7,8]
diccionario = {1: 'pedro', 2: 'oscar',3:'pepe'}
funcd(lista,diccionario)
