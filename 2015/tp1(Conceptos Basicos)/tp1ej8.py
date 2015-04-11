# coding=utf-8
__author__ = 'guillermo'
"""8. ¿Qué diferencia existe en representar el tipo string con comillas simples y dobles? ¿Para
qué sirven las secuencias de escape? ¿Es lo mismo imprimir “a\na” que “a\\na”? ¿Existe
alguna manera de obtener el mismo resultado sin escribir \\?

Las cadenas de texto, o strings, las delimitamos en Python encerrándolas entre comillas. Por lo general, estas pueden ser simples o dobles, da igual cuáles
empleemos (con la condición de que la comilla que abre sea del mismo tipo que la que cierra, por supuesto). En los ejemplos que he incluido en esta serie me
habréis visto usar un tipo u otro indistintamente.
La ventaja de poder elegir entre comillas simples o dobles la encontramos cuando necesitemos anidar unas comillas dentro de otras. Observad el siguiente ejemplo:

Por ejemplo:
>>> >>> print('Una de mis series favoritas era "La casa de la pradera".')
Una de mis series favoritas era "La casa de la pradera".

Esto lo hemos podido conseguir utilizando el par interior de comillas de tipo diferente a la que abre y cierra el string, de modo que Python no puede
confundirse a la hora de delimitar el fin de la cadena.

Pero, ¿como haríamos si necesitáramos imprimir las propias comillas simples o dobles, con libertad, dentro de un string?
La solución pasa por utilizar “caracteres de escape”. Referenciamos las comillas simples y dobles precediéndolas de un backslash (\), de modo que Python
ignore su significado habitual delimitando strings.

Para escribir una comilla simple, emplearíamos \’ y, para una doble, \”.

Por ejemplo:

>>> print('Una de mis canciones favoritas de Beatles es "Maxwell\'s silver hammer".')
Una de mis canciones favoritas de Beatles es "Maxwell's silver hammer".

2-Las secuencias de escape permiten introducir caracteres especiales, escapándolos (forzándolos a ser caracteres sin significado especial) con una
contrabarra (\) delante.
3-No es lo mismo ya que a\na” imprime una a abajo de la otra encambio a\\na me provoca tener una barra invertida
4-Si pero no tiene q ser seguido de ninguna letra que incluya una secuencia de escape
"""

print 'a\na'
print 'a\\na'

print 'a\sdf'