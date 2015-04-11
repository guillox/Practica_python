"""6.- a) Sea un diccionario como el visto en 4.- b), escriba un script que recorra la estructura y para 
aquellas personas que tienen más de 18 años cree una tupla con su nombre y la frase “Mayor de edad”y para 
aquellos que no lo sean su nombre y “Menor de edad”, y por último su edad y la ubique en la misma posición 
del diccionario.Por ejemplo, se espera que se generen tuplas con el siguiente formato:
('Alberto', 'Mayor de edad', 40)
4a-4.- a) Describir qué hacen las siguientes sentencias:
fori in range(1, 10):
printi
else:''
print 'Termino el bucle'
4b) Modificar las sentencias de a) para que informe dentro del rango del 2 al 30 
(inclusive) qué números son pares y cuáles impares.
"""

for i in range(1, 10):
  if (i % 2)==0:
  	print 'par'+str(i) 
  else:
     print 'impar' + str(i)
     