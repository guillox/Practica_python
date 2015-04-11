"""Nota: Controle que N >= 0. El programa no debe continuar mientras N no cumple esa condición (utilizar bucle).
e) Modifique d) para que si en algún momento determinado la suma de los números impares da mayor que 50 corte 
la ejecución del bucle. Nuevamente resuélvalo utilizando while y for..in."""

suma=0
N=int(raw_input('Ingrese un numero entero'))
base=int(raw_input('Ingrese un numero base'))
for i in  range(base,N):
	if (i%2)==1:
		suma=suma+i
	if suma >=50
		break	
print suma		


sumawhile=0
while (base<=N) and (sumawhile<=50) :
	if i % 2==0:
		sumawhile=sumawhile+i
print sumawhile


sumawhile=0
while (base<=N)  :
	if i % 2==0:
		sumawhile=sumawhile+i
	if sumawhile>=50
		break	
print sumawhile