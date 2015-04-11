import time
frase = raw_input('ingrese una frase:')
palabra = raw_input('ingrese una palabra:')
if frase.find(palabra) != -1:
    print frase.find(palabra)
else:
    print('no se encontro la frase')
print frase.count('.')
time.sleep(5)