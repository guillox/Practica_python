"""9.- a) Implemente  una calculadora simple, en donde se ingrese (por entrada estandar) dos operandos  y  
el  operador(+,-,*, /) e imprima el valor de la operacion resultante(por el momento no tenga en cuenta errores 
de tipos, ej: que el operando no sea numero o que el operador no sea los enumerados).
Nota: No codifique con condicionales (if, elif, etc) ni bucles (while, for, etc)"""

var_ent1= int(raw_input("ingrese un valor entero"))
var_ent2= int(raw_input("ingrese un valor entero"))
var_oper= raw_input("ingrese un valor del operando")
eval("var_ent1 var_oper var_ent2")
