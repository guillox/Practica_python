"""10.-  Implemente una clase Punto que represente un punto cartesiano (x, y) y que posea un
método distancia() que reciba como parámetro otro punto y calcule la distancia entre ambos.
(Sean  P
1(x1, y1)  y  P2( x2, y2)  la  distancia  entre  ambos  es  igual  a √ ( x2− x1)2+ ( y2− y1)2)

math.sqrt(x)


"""

import math


class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, objeto2):
        return math.sqrt((objeto2.getx() - self.x) ** 2 + (objeto2.gety() - self.y) ** 2)

    def getx(self):
        return self.x

    def gety(self):
        return self.y


objeto1 = Punto(10, 2)  # Creacion del objeto 1(instaciacion)
objeto2 = Punto(5, 3)  # Creacion del objeto 2(instanciacion)
print(objeto2.distancia(objeto1))
