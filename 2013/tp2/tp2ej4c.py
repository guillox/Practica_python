"""c) Ahora imprima la suma de los primeros N números impares, siendo N un 
entero ingresado por la entrada estándar. Resuelvalo utilizando tanto for..in
como while."""
suma=0
N=int(raw_input('Ingrese un numero entero'))
for i in  range(N):
	if (i%2)==1:
		suma=suma+i
print suma		

sumawhile=0
while (i<=N):
	if i % 2==0:
		suma=sumawhile+i
print sumawhile
