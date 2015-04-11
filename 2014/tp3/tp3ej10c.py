__author__ = 'guillermo'

"""idem anterior pero de otra forma"""

import math


class Punto:  # Clase punto
    def __init__(self, x, y):
        self.y = y
        self.x = x


    def reiniciar(self):  # metodo reiniciar
        self.mover(0, 0)

    def calcular_distancia(self, otro_punto):  # metodo reiniciar
        """

        :param otro_punto: otro punto que seria el punto2
        :return: la distancia entre el punto1 y el punto2
        """
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)


punto1 = Punto(10, 2)
punto2 = Punto(5, 3)
# punto1.reiniciar()

print ((punto2.calcular_distancia(punto1)))
