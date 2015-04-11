"""2.- a) Explique la semántica de los bucles while y for..in. Transcriba los ejemplos vistos en teoría en un 
módulo Python y ejecútelos."""


num=0
while (num<20):
	if num % 2==0:
		print str(num) + "es uno de los primeros numero pares"
	num=num+1
	
lista=["el","for","ha","recorrido","toda","la","lista"]		
for elemento in lista :
	print elemento

