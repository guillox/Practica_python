"""b) Modificar las sentencias de a) para que informe dentro del rango del 2 al 30 
(inclusive) qué números son pares y cuáles impares."""

for i in range(1, 10):
  if (i % 2)==0:
  	print 'par'+str(i) 
  else:
     print 'impar' + str(i)
