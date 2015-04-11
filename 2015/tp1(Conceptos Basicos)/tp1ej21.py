# coding=utf-8
__author__ = 'guillermo'
"""21. Arme una lista con información de las carreras de grado y posgrado de la Facultad de
Informática. De cada carrera se desea guardar su nombre, duración y cantidad de
materias del plan. ¿Cómo haría para agregarle los diferentes planes a cada carrera?appens
¿Cómo diferenciaría las carreras de grado y posgrado? (por el nombre de la lista) Imprima la cantidad de planes
diferentes de la primeras dos carreras de la lista y la duración de la última."""

listacgrado = []
listacpostgrado=[]
nombre = raw_input('ingrese el nombre de la carrera:')
duracion = int(raw_input('Ingrese el duracion de la carrera:'))
cantidad = int(raw_input('Ingrese la cantidad de materias del plan:'))
listacgrado.append([nombre, duracion, cantidad])
nombre = raw_input('ingrese el nombre de la carrera:')
duracion = int(raw_input('Ingrese el duracion de la carrera:'))
cantidad = int(raw_input('Ingrese la cantidad de materias del plan:'))
listacgrado.append([nombre, duracion, cantidad])
nombre = raw_input('ingrese el nombre de la carrera:')
duracion = int(raw_input('Ingrese el duracion de la carrera:'))
cantidad = int(raw_input('Ingrese la cantidad de materias del plan:'))
listacgrado.append([nombre, duracion, cantidad])
print listacgrado
nombre = raw_input('ingrese el nombre de la carrera:')
duracion = int(raw_input('Ingrese el duracion de la carrera:'))
cantidad = int(raw_input('Ingrese la cantidad de materias del plan:'))
listacpostgrado.append([nombre, duracion, cantidad])
nombre = raw_input('ingrese el nombre de la carrera:')
duracion = int(raw_input('Ingrese el duracion de la carrera:'))
cantidad = int(raw_input('Ingrese la cantidad de materias del plan:'))
listacpostgrado.append([nombre, duracion, cantidad])
nombre = raw_input('ingrese el nombre de la carrera:')
duracion = int(raw_input('Ingrese el duracion de la carrera:'))
cantidad = int(raw_input('Ingrese la cantidad de materias del plan:'))
listacpostgrado.append([nombre, duracion, cantidad])
print listacpostgrado
print 'cantidad de planes de la primer carrera (grado):', listacgrado[0][2], 'cantidad de planes de la primer carrera:(grado)', listacgrado[1][2]
print 'cantidad de planes de la primer carrera (posgrado):', listacpostgrado[0][2], 'cantidad de planes de la primer carrera (posgrado):',listacpostgrado[1][2]
print 'duracion de la ultima carrera (grado):', listacgrado[-1][1],'duracion de la penultima carrera (grado):', listacgrado[-2][1]
print 'duracion de la ultima carrera (postgrado):', listacpostgrado[-1][1], 'duracion de la ultima carrera (postgrado):', listacpostgrado[-2][1]




