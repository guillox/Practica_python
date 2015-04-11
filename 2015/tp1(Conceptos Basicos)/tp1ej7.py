# coding=utf-8
__author__ = 'guillermo marti'
"""7. Explique qué hacen las siguientes instrucciones. Ejecute las mismas tanto con Python 2.x
como 3.x. ¿Encuentra diferencias?(python 2.x)
a. x = y = z = 20
b. x = “Hola” * 3
c. y = “Hola” + 3
d. x = 7 / 3
e. x = 7.0 / 3
f. x = int(7.0) // 3
g. cadena = “Hola” + ‘profe’
h. linea = “hola” + ‘\n’ + ‘profe’
i. x = chr(65) + chr(66) + chr(67)
j. a = 5L + 2L

k. y = xrange(5)
Python tiene otra función rango llamado xrange () . La sintaxis de xrange () es exactamente el mismo que el rango (), pero xrange ()
rellena su lista banda, cuando se accede a ella, permitiendo que la memoria que se libera cuando la lista no se utiliza activamente.
Una cosa más que añadir. En Python 3.x, el xrange función ya no existe más. El rango de la función ahora hace lo xrange hace en Python 2.x, así que para mantener tu portátil de código, es posible que desee adherirse a la utilización de rango en su lugar. Por supuesto, siempre se puede utilizar el 2to3 herramienta que Python proporciona con el fin de convertir su código, pero que presenta una mayor complejidad.
La razón por la xrange se retiró fue porque es básicamente siempre es mejor usarlo, y los efectos en el rendimiento son
insignificantes. Así de Python 3.x gama función es xrange de Python 2.x
l. x = `4+5`
m. a = round(2.5) + 4

"""

x = y = z = 20
print x, y, z  # inicializo tres variables con el mismo valor
x = "Hola" * 3
print x  # imprimo hola 3 veces
# y = "Hola" + 3
#print y #me da error ya que quiero trabajar con un string y un entero
x = 7 / 3
print x  # me obtiene la division entera en python 2 en cambio en python 3 es fraccionaria
x = 7.0 / 3
print x  # me obtiene la division fraccionaria
x = int(7.0) // 3
print x  # resultado será de tipo entero o decimal dependiendo del tipo de los números empleados (pero en caso de ser decimal, la parte decimal será cero)
cadena = "Hola" + 'profe'
print cadena  # concatena el string hola con el string profe
linea = "hola" + '\n' + 'profe'
print linea  # me crea un interlineado entre las dos palabras
x = chr(65) + chr(66) + chr(67)
print x  # me convirte el numero en caracter y lo ccncateno
a = 5L + 2L
print a # imprime el resultado de 5 + 2 pero ambos son enteros largos
y = xrange(5)
print y
x = '4+5'
print x # imprime 4 + 5 pero como caracter
a = round(2.5) + 4
print a # round redondea un numero al mas proximo entero