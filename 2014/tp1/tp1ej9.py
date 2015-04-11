#) Implemente una calculadora simple, en donde se ingrese (por entrada estándar string) dos                        
#operandos y el operador (+ , - , * , / ) e imprima el valor de la operación resultante.
# Nota 1: por el momento, no tenga en cuenta errores de tipos – ej: que el operando no                                  
# sea número o que el operador no esté entre los enumerados.
#Nota 2: El código no debe contener condicionales (i f , e l i f , etc) ni bucles (f o r ,                          
#w h i l e , etc)
# Ayuda: Investigue el comando e v a l ( )

num1 = raw_input ('ingrese el numero 1 ')
num2= raw_input ('ingrese el numero 2 ')
operador=raw_input('ingrese el operador ')
print eval('num1 + operador + num2')






