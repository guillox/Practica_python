'''b) A la calculadora implementada en a) agréguele la capacidad de calcular la potencia,                          
parte entera y resto de la división. ¿Tuvo que modificar el código realizado en a)? **(potencia) %(resto)
no es necesario modificar el codigo'''

num1 = raw_input ('ingrese el numero 1: ')
num2= raw_input ('ingrese el numero 2: ')
operador=raw_input('ingrese el operador')

print eval(num1 + operador + num2)
