"""b) Desarrolle mediante funciones y listas el funcionamiento de las colas FIFO (el 
primero en entrar es el primero en salir) con sus operaciones pop, push(introduce a la cola) y length(tamaño) 
recibiendo la lista como parámetro. En la función push si no se envía como parámetro 
ningún elemento por defecto el valor será 0 (cero).
«primero en llegar, primero en ser atendido» (del inglés first come, first served o FCFS)"""

def fcolapush(lista,lista2,i):
	return lista2.append(lista(i))

	



lista=[22,true,"una lista",[1,2]]
lista2=[]
for i in range(1,len(lista)):
	fcolapush(lista2,i)