__author__ = 'guillermo'


def imprimosaludo(nombre):
    print('saludo para:' + nombre + 'correcto')


imprimosaludo('')

a = 2
b = 3


def cambio(a, b):
    x = a
    a = b
    b = x
    return a, b


print(cambio(a, b))


def cambio(x):
    x[0] = 'cero'


a = [1, 2, 3]
cambio(a)
print(a)