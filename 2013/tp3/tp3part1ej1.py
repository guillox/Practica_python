"""Manejo de archivos
Parte I
1.- Dado un conjunto de números (que se tomarán de la entrada estándar), generar dos archivos:
uno con los números  pares y otro con los impares."""

L = [1,2,3,4,5,5] 
conjuntoL = set(L)
def creacion():
	archimp=open("archivo.txt","w")
	archimp.close()
	archpar=open("archivo txt","w")
	archpar.close()


def escpar(listapar):
	archpar=open("archivopar.txt","a")
	for p in range(1,len(listapar)):
    	archpar.write(listapar[p])
	archpar.close
def escimp(listapar):
	archimp=open("archivoimp.txt","a")
	for i in range(1,len(listaimpar)):
		archimp.write(listaimpar[p])
	archimp.close

			

creacion()
Listapar=[]
listaimp=[]
for x in range(1,len(L)):
	if L[x]%2==0:
		Listapar.append(L[x])
	else:
		listaimp.append(l[x])

escpar(listapar)
escimp(listimp)
	
			