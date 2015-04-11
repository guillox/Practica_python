"""
1
c) Modifique b) para que el valor de la nota sea ingresado por la entrada estándar.

"""

num = input('ingrese la nota')
if num < 4:
    print("DESAPROBADO")
elif num >= 4 and num <= 10:
    print("APROBADO")
else:
    print("El valor ingresado no corresponde a una nota")