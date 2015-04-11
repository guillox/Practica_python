"""d) Modifique c) para que además del número N, se obtenga a partir de qué 
número se quiere empezar a buscar los impares, es decir si N = 10 y base = 5 
buscaremos los 10 primeros números impares a partir del 5 y retornaremos la 
suma de ellos. Elija el bucle que crea más conveniente."""

suma=0
N=int(raw_input('Ingrese un numero entero'))
base=int(raw_input('Ingrese un numero base'))
for i in  range(base,N):
	if (i%2)==1:
		suma=suma+i
print suma		

sumawhile=0
while (base<=N):
	if i % 2==0:
		suma=sumawhile+i
print sumawhile
