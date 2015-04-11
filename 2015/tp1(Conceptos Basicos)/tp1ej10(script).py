import time
frase = raw_input('ingrese una frase:')
palabra = raw_input('ingrese una palabra:')
if frase.find(palabra) != -1:
    print palabra.find(palabra)
else:
    print('no se encontro la frase')
time.sleep(5)