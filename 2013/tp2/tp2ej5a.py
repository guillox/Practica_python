# -*- coding: utf-8 -*-
"""5.- a) Dada una lista con N números, modifique dicha lista multiplicando por 2 cada uno 
de los elementos. Es decir, si tengo [2, 3, 4, 5, 6] el resultado sería [4, 6, 8, 10, 12]."""

lista=[2, 3, 4, 5, 6]
for i in range(0,len(lista)-1):
	lista[i]=lista[i]*2 
	print lista[i]
