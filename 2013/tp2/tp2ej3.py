"""3.- Modifique el ejercicio 11.- c) de la Práctica 1 para que se lean los alumnos y las 
notas de teclado, informándolas hasta que se encuentre el número -1, y al finalizar 
deberá imprimir "Fin de la carga de notas"""

alumnos=raw_input('ingrese en nombre del alumno')
nota=int(raw_input('ingrese la nota del alumno'))
while nota!= -1:
	alumnos=raw_input('ingrese en nombre del alumno')
	nota=int(raw_input('ingrese la nota del alumno'))
print "Fin de la carga de notas"
	