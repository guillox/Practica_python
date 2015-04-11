"""
b) Escriba el código necesario para que dada una variable con un valor entero, si este 
es más chico que 4 imprima “DESAPROBADO”; si el valor está entre 4 y 10 imprima 
“APROBADO”; y ante cualquier otro valor imprima “El valor ingresado no corresponde a 
una nota”.
"""
num = 4
if num < 4:
    print("DESAPROBADO")
elif num >= 4 and num <= 10:
    print("APROBADO")
else:
    print("El valor ingresado no corresponde a una nota")

