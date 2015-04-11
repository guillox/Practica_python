# coding=utf-8
__author__ = 'guillermo'

"""18. Dado un número hexadecimal y otro binario cualquiera, imprima la suma y el producto
de ambos en base binaria, octal, decimal y hexadecimal.

De binario a decimal.

b = 11001
#Convertimos el entero en una cadena y despeas lo pasamos a binario.
#Base 2.
print int(str(b), 2)
>>> 25

"""

numh = 23
numb = 100111
print 'imprime la suma entre numh y numb en binario:', bin(int(str(numh), 8) + int(str(numb), 2))
print 'imprime la multiplicacion entre numh y numb en binario:', bin(int(str(numh), 8) * int(str(numb), 2))
print 'imprime la suma entre numh y numb en octal:', oct(int(str(numh), 8) + int(str(numb), 2))
print 'imprime la multiplicacion entre numh y numb en octal:', oct(int(str(numh), 8) * int(str(numb), 2))
print 'imprime la suma entre numh y numb en octal:', hex(int(str(numh), 8) + int(str(numb), 2))
print 'imprime la multiplicacion entre numh y numb en octal:', hex(int(str(numh), 8) * int(str(numb), 2))



