"""
14.- Conjuntos
d) Sea el siguiente código:
conjunto  =  set([1,2,3,4,5,6])
II. Agregue el elemento 4 e imprima los elementos del conjunto. ¿Hubo alguna                        
modificación? ¿Por qué?
http://elclubdelautodidacta.es/wp/2012/06/python-agregacion-y-eliminacion-de-elementos-de-un-conjunto/
no se modifico pq se compone de una lista no ordenada de datos en la cual no hay ningún dato repetido

"""

conjunto  =  set([1,2,3,4,5,6])
elem=input('ingrese un elemento')
conjunto.add(elem)
print conjunto