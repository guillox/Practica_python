"""
14.- Conjuntos
d) Sea el siguiente código:
conjunto  =  set([1,2,3,4,5,6])
III. Realice la intersección, unión y diferencia del conjunto dado con este otro:
set([3,4 ,5,10,15])

ejemplo
>>> c1 = {1, 2, 3, 4, 5, 6}
>>> c2 = {2, 4, 6, 8, 10}
>>> c3 = {1, 2, 3}
>>> c4 = {4, 5, 6}

union
>>> c1 | c2
{1, 2, 3, 4, 5, 6, 8, 10}

union(otraforma)
>>> c1.union(c2)
{1, 2, 3, 4, 5, 6, 8, 10}

union mas de dos operandos
>>> c1 | c2 | c3
{1, 2, 3, 4, 5, 6, 8, 10}

intersección
>>> c1 & c2
{2, 4, 6}

intersección(otraforma)
>>> c1.intersection(c2, c3)
{2}

intersección mas de dos operandos
>>> c1 & c2 & c3 & c4
set()       # El conjunto vacío

diferencia
>>> c1 - c2   
{1, 3, 5}
diferencia otra forma
>>> c1.difference(c2)
{1, 3, 5}

union exclusiva o diferencia simetrica
>>> c1 ^ c2
{1, 3, 5, 8, 10}

union exclusiva o diferencia simetrica(otraforma)
>>> c1.symmetric_difference(c2)
{1, 3, 5, 8, 10}

"""
conjunto1  =  set([1,2,3,4,5,6])
conjunto2   =set([3,4 ,5,10,15])
print  conjunto1 & conjunto2
print  conjunto1 | conjunto2
print  conjunto1 - conjunto2

