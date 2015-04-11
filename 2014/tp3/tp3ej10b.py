__author__ = 'guillermo'

"""idem anterior pero de otra forma"""

import math


class Punto:  # Clase punto
    def mover(self, x, y):  # metodo mover
        self.x = x
        self.y = y

    def reiniciar(self):  # metodo reiniciar
        self.mover(0, 0)

    def calcular_distancia(self, otro_punto):# metodo reiniciar
        """

        :param otro_punto: otro punto que seria el punto2
        :return: la distancia entre el punto1 y el punto2
        """
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)


punto1 = Punto()
punto2 = Punto()
# punto1.reiniciar()
punto1.mover(10, 2)
punto2.mover(5, 3)
print ((punto2.calcular_distancia(punto1)))
