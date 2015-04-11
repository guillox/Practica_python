""" 4.- Escriba un módulo que provea la funcionalidad de almacenar en un archivo nombres de  personas y sus
 edades. Además realice una función que busque en el archivo e imprima un listado de todos los nombres cuya 
 edad sea mayor a un número determinado."""

def creararchivo(archiinfo)
	archiinfo=open("infoper.txt","W")"""se abre un archivo modo lectrura"""
	nombre=raw_input('ingrese el nombre de la persona')
	edad=raw_input('ingrese la edad de la persona')
	while edad!=-1:
		archiinfo.write(nombre,edad)
		nombre=raw_input('ingrese el nombre de la persona')
		edad=raw_input('ingrese la edad de la persona')
	archiinfo.close()

def buscar(archiinfo)
	archiinfo.open("infoper.txt","R")
	buscar=int(raw_input("ingrese un numero determinado:"))
    
    for i in file.readlines():
     if i.find(search) >= 0:
        print "Caracter Encontrado";
     else:
        print "Caracter No Encontrado";
file.close()

 creararchivo(archiinfo)
 buscar(archiinfo)