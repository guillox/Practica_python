"""
6.- a) Sea un diccionario como el visto en 4.- b), escriba un script que recorra la estructura y para aquellas
personas que tienen más de 18 años cree una tupla con su nombre y la frase “Mayor de edad” y para aquellos
que no lo sean su nombre y “Menor de edad”, y por último su edad y la ubique en la misma posición del
diccionario.
Por ejemplo, se espera que se generen tuplas con el siguiente formato:
('Alberto', 'Mayor de edad', 40)

ejemplo
macedonia
{'fresa': 'roja', 'plátano': 'amarillo', 'manzana': 'verde'}
Empleando el método keys():

frutas = macedonia.keys()
 frutas
dict_keys(['fresa', 'plátano'])

for fruta in frutas:
  print(fruta)

  
fresa
plátano
manzana

metodo value ()
colores = macedonia.values()
colores
dict_values(['roja', 'amarillo', 'verde'])

for color in colores:
  print(color)

  
roja
amarillo
verde

values() Devuelve una lista de los valores del diccionario.

python 2.x

 diccionario.values()
[2, 3, 2]

python 3.x

list(diccionario.values())
[2, 3, 2]

keys() Devuelve una lista de las claves del diccionario.

python 2.x

diccionario.keys()
['enero', 'marzo', 'febero']

python 3.x

list(diccionario.keys())
['enero', 'marzo', 'febero']
"""

personas = {'Jose': 15, 'Guillermo': 26, 'Maria': 10, 'julia': 35}

#print ((personas.values())
print(type((list(personas.values()))))
for pers in personas:
    if personas.values(pers) >= 18:
        t = t + list((personas.keys(pers)), 'Mayor de edad', list(personas.values(pers)))
    else:
        t = t + list((personas.keys(pers)), 'Menor de edad', list(personas.values(pers)))
print(t)

























