# -*- coding: utf-8 -*-
__author__ = 'guillermo'

"""
4. Defia las siguientes funciones para el ejercicio 4 de la práctia 2:
a. agregar_evento(eventos, datos): Agregar los “datos” de un evento a la
estructura de datos “eventos”
b. agregar_invitado(eventos, nom, desc_event): Agrega en “eventos” un invitado
de nombre “nom” al evento con descripción “desc_event”
c. confimar_presencia(eventos, nom, desc_event): Confima la presencia del
invitado de nombre “nom” al evento con descripción “desc_event” en “eventos”

4. Defia las siguientes funciones para el ejercicio 4 de la práctia 2:
a. agregar_evento(eventos, datos): Agregar los “datos” de un evento a la estructura de datos “eventos”
b. agregar_invitado(eventos, nom, desc_event): Agrega en “eventos” un invitado de nombre “nom” al evento con descripción
“desc_event”
c. confimar_presencia(eventos, nom, desc_event): Confima la presencia delinvitado de nombre “nom” al evento con
descripción “desc_event” en “eventos”"""

def agregar_evento(eventos, datos):


eventos = [{'descripcion':'casamiento', 'fecha' :'12/23/15', 'hora': 16, 'listainvt': ['carlos', 'pedro', 'roberto', 'maria', 'laura','raul'],
            'publico':False}, {'descripcion': 'quinse', 'fecha': '10/12/15', 'hora': 22, 'listainvt': ['juan', 'carla', 'lucrecia', 'catalina', 'guillermo'],
            'publico':False}]

datos=[[]]
j = 0
infodesc = raw_input('ingrese descripcion del evento:')
while (infodesc != 'fin'):
    for i in range(0, len(eventos[j].keys())):
        datos[i].append(infodesc)
        infofecha = raw_input('ingrese fecha del evento:')
        datos[i].append(infofecha)
        infohora = raw_input('ingrese hora del evento:')
        datos[i].append(infohora)
        infoinv = raw_input('ingrese infoinv del evento:')
        while infoinv != 'fin':
            datos[i][]


agregar_evento(eventos, datos)

#a. agregar_evento(eventos, datos): Agregar los “datos” de un evento a la estructura de datos “eventos”

# imprima la cantidad de invitados de alguno en particular
print 'la cantidad de invitados de un evento es: ', len(eventos[0]['listainvt'])

#agréguele dos invitados

for i in range(0, 2):
    inv = raw_input('ingrese un nuevo invitado: ')
    (eventos[0]['listainvt']).append(inv)

print eventos

#elimine uno de otro evento.

print (eventos[1]['listainvt']).pop(2)
print (eventos[1]['listainvt'])

#¿Cómo haría si quisiera agregarle un estado a los invitados que indique si el mismo confirmó asistencia, aún no la
# confirmó o bien la rechazó? Modifique la estructura para ello

lista = (eventos[0]['listainvt'])
del eventos[0]['listainvt']
print eventos[0]
for i in range(0, len(lista)):
    estado = raw_input('ingrese un estado: ')
    eventos[0][lista[i]] = estado

print eventos[0]

