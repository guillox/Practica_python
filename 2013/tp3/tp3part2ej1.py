""" Parte II - Ejercicio a entregar: manejo de calendario de cumpleaños Se necesita manejar un calendario de 
cumpleaños donde se pueda almacenar la siguiente información:
				● Fecha de cumpleaños
				● Nombre del cumpleañero
				● Medio de contacto (1 por cumpleaños): compuesto por:
					○ Tipo de contacto: por ejemplo “email”, “teléfono”, “celular”, “dirección”
					○ Medio de contacto: por ejemplo “jorge@example.com”, “(0221) 423-2030”,
					“(0221) 15 567-8910”, “50 y 120” respectivamente.
Esta información debe ser persistida en un archivo utilizando alguna estructura que permita realizar las 
siguientes operaciones:
				● Búsqueda por fecha de cumpleaños o por nombre del cumpleañero
				● Cargar un nuevo cumpleaños
				● Borrar un cumpleaños
Al persistir información en archivos de texto plano, estos pueden ser leídos y manipulados con cualquier editor 
(editPlus, vi, vim, gedit, blocdenotas,etc.).Es por eso que se deberá encriptar la información que seguarda. 
Para ello proponemos diferentes técnicas sencillas parapoder implementarlo:

1. Utilizando las funciones ord()y chr(): se pueden manipular los valores de cada uno de los caracteres de forma 
que lo que se vea no es realmente lo que es. Pongamos un ejemplo; si tenemos la palabra “python” podríamos 
efectuar un tratamiento carácter por carácter convirtiendo(incrementando o decrementando) su valor ASCII, si 
acada carácter sele resta 30 del código ASCII quedaría así “R[VJQP” y de esta forma sería como podríamos 
almacenar lo dificultando la tarea de comprensión del archivo.Luego para desencriptar lo haríamos la función 
inversa: tomcaracter por caracter,se lo convierte a valores ASCII y se les suma 30 quedando nuevamente la palabra 
“python”.

2. Usando la función maketrans(): dicha función realiza una conversión simultánea de los caracteres basados en 
una tabla de conversión que es provista por el programador. Se necesita la tabla para encriptar y una tabla para                        
desencriptar. Para que funcione correctamente una debe ser la inversa de la otra.

3. Pasando cada dígito a binario y separar lo por un caracteres especial: primero se debería convertir cada carácter 
a su correspondiente códigoASCII, y luego se podría convertir dicho valor a binario para guardarlo, separando 
cada caracter, por ejemplo, conunguión(-). De estamanera, para desencriptar lo se podría guardar en una lista cada 
número separado por guión, convertirlo a decimal y obtener su correspondiente carácter ASCII.

4. Usando un módulo de compresión: importando algún módulo de compresión como el zlib, gzipo el bz2 se puede 
comprimir un string mediante la función compress(), lo que permite reducir su espacio físico una vez almacenado
y que además su código es ilegible. Luego se puede descomprimir cada string utilizando la función decompress().    
(http://docs.python.org/tutorial/stdlib.html#data-compression)
Adicionalmente se requiere compartir la información entre distintas aplicaciones, para ello se                    
pide que se desarrolle la exportación del calendario en formato iCalendar. Una vez que se obtenga el archivo 
con la exportación de los eventos creados(cumpleaños) se debe probar en alguna aplicación que soporte este 
formato.
Informacion sobre iCalendar http://es.wikipedia.org/wiki/ICalendar

Nota1: Cada grupo va a tener asignado un método de encriptación. La asignación será en base                              
a la siguiente función que deberán correr en un módulo para averiguar qué método deben implementar:
x = int(raw_input('Ingrese su numero de grupo: '))
print (x%4) if (x%4!=0) else 4
Nota2: Recomendamos la utilización de Pickle para guardar las estructuras completas en el archivo 
(http://docs.python.org/library/pickle.html). permite serializar casi cualquier objeto(objetos de tipos definidos 
	por el usuario, colecciones que contienen colecciones,etc) y cuenta algunos mecanimos de seguridad """


-*- coding: utf-8 -*-
python setup.py install
import pickle
import icalendar
import zlib

# *** no esta completo de lo del iCal

 cal = Calendar()
 from datetime import date
 cal.add('prodid', '-//My calendar product//mxm.dk//')
 cal.add('version', '2.0')

 import pytz
 
    event = icalendar.cal.Event() # Creo un evento
    event.add('summary', 'Python meeting about calendaring')
    event.add('dtstart', date(2005,1,1,0,0,0,tzinfo=pytz.utc))# Especifico la fecha de inicio
    event.add('rrule', { 'freq': 'yearly', 'interval': 1 })# Expecifico que es un evento recursivo cada 1 año
    
    
 cal.add_component(event)

 c = open('calendar.ics', 'wb')
 c.write(cal.to_ical(f))
 c.close()


def crear_calendario():#crear un nuevo calendario
    dic = {}
    f = open("calendario.txt", "w")#abrir el archivo modo escritura
    pickle.dump(dic,f)#trabaja con una cadena en vez de un archivo donde lo q tiene dic se lo da a f
    f.close()#cerrar el archivo modo lectura
   
def encriptar(esto):
    palabra = ""
    for x in esto:
        palabra = palabra + str(bin(ord(x))) + "-" #tener en cuenta que queda con una raya demas
    return palabra
 
def desencriptar(esto):
    lista = esto.split("-")
    lista.pop() #Esto es para que se borre la ultima raya
    palabra = ""
    for x in lista:
        palabra = palabra + str(chr(eval(x)))
    return palabra
                               
def agregar_cumple():
    print "***Ingrese los datos del cumpleanios***"
    fecha = zlib.compress(encriptar(raw_input("Fecha: ")))
    nombre = zlib.compress(encriptar(raw_input("Nombre: ")))
    tipo = zlib.compress(encriptar(raw_input("tipo de contacto: ")))
    medio = zlib.compress(encriptar(raw_input("Medio de contacto: ")))
    try:
        f = open("calendario.txt", "r") #abre un archivo de texto en modo lectura
    except:
        crear_calendario()
        print ("Se ha creado un nuevo calendario")
        f = open("calendario.txt","r") #abre un archivo de texto en modo lectura
    finally:#El código colocado en la cláusula finally se ejecuta siemprese haya o no levantado una excepción
        agenda = pickle.load(f) #la funcion load carga el objeto serializado, ya q este es una lista
        if fecha in agenda.keys():#devuelve una lista de todas las claves usadas en el diccionario
            agenda[fecha].append((nombre, tipo, medio))#Añade un objeto al final de la lista

        else:#El código colocado en la cláusula else se ejecuta solo si no se levante una excepción
            agenda[fecha] = [(nombre, tipo, medio)]
        f.close()#cierra el archivo
        f = open("calendario.txt", "w")#abre el archivo de modo escritura
        pickle.dump(agenda, f)#trabaja con una cadena en vez de un archivo donde lo q tiene agenda se lo da a f
        f.close()#cierra el archivo
        print "Se ha agregado el cumple de " + zlib.decompress(desencriptar(nombre)) + " a la agenda"
        print " "
 
def buscar_cumple():
    print "Ingrese 1 para buscar por nombre o 2 para buscar por fecha de cumpleanos (cualquier otro caracter para cancelar)"
    op = raw_input("Opcion:")
    if op == "1":
        try:
            f = open("calendario.txt","r")#Abre el archivo de modo lectura
        except:
            print "aun no ha ingresado ningun cumple!"
        else#El código colocado en la cláusula else se ejecuta solo si no se levante una excepción:
            print "Ingrese el nombre"
            nomb = zlib.compress(encriptar(raw_input("Nombre:")))
            dic = pickle.load(f)#la funcion load carga el objeto serializado, ya q este es una lista
            f.close()#cerrar el archivo
            encontrado = "no"
            for i in dic.keys():#devuelve una lista de todas las claves usadas en el diccionario
                for j in range(len(dic[i])):            
                    if nomb == dic[i][j][0]:
                        print ("Se encontro " + zlib.decompress(desencriptar(dic[i][j][0])) + " el dia " + zlib.decompress(desencriptar(i)))
                        encontrado = "si"
            if encontrado == "no":
                print "***No se hayaron coinsidencias***"
       
    elif op == "2":
        try:
            f = open("calendario.txt","r")#abre el archivo modo lectura
        except:
            print "aun no ha ingresado ningun cumple!"
        else#• El código colocado en la cláusula else se ejecuta solo si no se levante una excepción:
            print "Ingrese la fecha"
            fecha = zlib.compress(encriptar(raw_input("Fecha: ")))
            dic = pickle.load(f)#la funcion load carga el objeto serializado, ya q este es una lista
            f.close()#Cierra el archivo
            if fecha in dic:
                for x in dic[fecha]:
                    print zlib.decompress(desencriptar (x[0])) + ", " + zlib.decompress(desencriptar (x[1])) + ", " + zlib.decompress(desencriptar (x[2])) + "\n"
   
   
def borrar_cumple():
    try:
        f = open("calendario.txt","r")#abre un archivo de modo lectura
    except:
        print "no se encontro el archivo calendario.txt"
    else# El código colocado en la cláusula else se ejecuta solo si no se levante una excepción:
        print "Ingrese el nombre y fecha del cumple a borrar"
        fecha = zlib.compress(encriptar(raw_input("Fecha:")))
        nomb = zlib.compress(encriptar(raw_input("Nombre:")))
        dic = pickle.load(f)
        f.close()#cierra el archivo
        if fecha in dic:
            i = 0
            while i < len(dic[fecha]) and dic[fecha][i][0] != nomb:
                    i = i + 1
            if i < len(dic[fecha]):
                del dic[fecha][i]
                if dic[fecha] == []:
                    del dic[fecha]
                f = open("calendario.txt","w")#abre archivo de modo escritura
                pickle.dump(dic, f)
                f.close()#cierra el archivo
            else:
                print "no se encontro el nombre " + zlib.decompress(desencriptar(nomb)) + " en la fecha " + zlib.decompress(desencriptar(fecha))
        else:
            print "no se ha encontrado ningun cumple en la fecha " + zlib.decompress(desencriptar(fecha))
 
############ Programa Principal ############
 
while 1:
        n= raw_input("¿Que desea hacer?\n 1: Agregar un cumple\n 2: Buscar un cumple\n 3: Borrar un cumple\n(Cualquier otra tecla para SALIR)\n")
        if n == "1":
            agregar_cumple()
        elif n== "2":
            buscar_cumple()
        elif n == "3":
            borrar_cumple()
        else:
            break