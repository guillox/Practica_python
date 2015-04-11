"""c) Modifique la calculadora para que reciba dos números enteros y un operando, que                          
pueden ser & , | o ^ y corresponden a AND , OR y XOR respectivamente, los transforme en                                
números binarios y calcule la operación ingresada y devuelva el resultado del cómputo tanto en                            
decimal como en binario.
bin(81) -> '0b1010001'
binario a decimal int('1010001', 2) -> 81
entero a string str(42)->42
"""

num1 = raw_input ('ingrese el numero 1: ')
num2= raw_input ('ingrese el numero 2: ')
operador=raw_input('ingrese el operador')
num1b= bin(int(num1))
num2b= bin(int(num2))
print num1b
print num2b
type(num1b)
type(num2b)
#resultado en binario
type(eval(str(num1b) + operador + str(num2b)))
print eval(str(num1b) + operador + str(num2b))
type(str(eval(str(num1b) + operador + str(num2b))))
#resultado en base decimal
#print int(str(eval(str(num1b) + operador + str(num2b))),2)

	
	
