"""13d. Sea el siguiente codigo:
conjunto= set([1,2,3,4,5,6])
iii. Realice la interseccion, union y diferencia del conjunto dado con este otro:
set([3,4,5,10,15])"""


conj1= set([1,2,3,4,5,6])
conj2= set([3,4,5,10,15])
#interseccion
print conj1 & conj2
#union 
print conj1 | conj2
#diferencia
print conj1.difference(conj2)
