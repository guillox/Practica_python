"""c) Modifique b) para que el valor de la nota sea ingresado por la entrada estándar."""

num=int(raw_input('ingrese un numero'))
if num < 4 :
	print "DESAPROBADO"
elif num>=4 and num<= 10: 
	print "aprobado"
else:
	 print"el valor ingresado no corresponde a una nota"