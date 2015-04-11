"""
1.­ Dado un conjunto de números (que se tomarán de la entrada estándar), generar dos                              
archivos: uno con los números pares y otro con los impares.
"""


def creararchivo():
	archpar=open("archivopar.txt",'w')
	archimpar=open("archivoimpar.txt",'w')
	archpar.close()
	archimpar.close()

def escribirarchivo(lista):
	archpar=open("archpar.txt",'a')
	archimpar=open('archivoimpar.txt','a')
	for x in range(len(lista)):
                if lista[x] % 2 == 0:
                        archpar.write(lista[x])
                else:
                        archimpar.write(lista[x])
	archpar.close();
	archimpar.close();		

def leerarchivo():
	archpar=open("archpar.txt",'r')
	archimpar=open('archivoimpar.txt','r')
	print (archpar.read())
	print (archivoimpar.read())
	archpar.close();
	archimpar.close();


num=int(input('ingrese un numero: '))
print (type(num))
lista=[]
while (num > 0):
	lista.append(num)
	num=int(input('ingrese un numero: '))
	
print (lista)

creararchivo()
escribirarchivo(lista)
leerarchivo()
