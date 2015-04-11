"""
c) Implemente una función que reciba una lista variable de números y un diccionario, y para cada elemento de la lista
imprima si el mismo es una clave del diccionario.



semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes',
 'Sábado', 'Domingo']

for dia in semana:
    print(dia)

---
Lunes
Martes
Miércoles
Jueves
Viernes
Sábado
Domingo

>> if 'Pedro' in gente:
  print(gente['Pedro'])
else:
  print('Esta clave no existe')

"""


def funcd(lista, diccionario):
    for elemento in lista:
        if elemento in diccionario.keys():
            print(elemento)


lista = [2, 4, 6, 7, 8]
diccionario = {1: 'pedro', 2: 'oscar', 3: 'pepe'}
funcd(lista, diccionario)

















