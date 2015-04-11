"""
14.- Conjuntos
d) Sea el siguiente código:
conjunto  =  set([1,2,3,4,5,6])
I. Agregue el elemento 7  e imprima los elementos del  conjunto
ejemplo
>>> c1 = set()     # El conjunto vacío
>>> c2 = {1, 2, 3, 4, 5, 6}

>>> c1.add('pimiento')
>>> c1
{'pimiento'}


"""

conjunto  =  set([1,2,3,4,5,6])
elem=input('ingrese un elemento')
conjunto.add(elem)
print conjunto
