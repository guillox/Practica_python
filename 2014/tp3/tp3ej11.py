"""11.-  A la clase del ejercicio anterior agréguele un método que verifique la igualdad entre dos
puntos. ¿Es lo mismo preguntar si dos objetos son iguales con el signo == que preguntándolo
con el método implementado? ¿Por qué? no es lo mismo ya que en el proceso de"""

import math


class Punto():
    def __init__(self, x, y):  # metodo de incializacion
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def distancia(self, objeto2):
        return math.sqrt((objeto2.getx() - self.x) ** 2 + (objeto2.gety() - self.y) ** 2)


    def igualdad(self, objeto2):
        if self.x - objeto2.getx() == 0 and self.y - objeto2.gety() == 0:
            return True
        return False


objeto1 = Punto(1, 1)  # Creacion del objeto 1(instaciacion)
objeto2 = Punto(1, 1)  # Creacion del objeto 2(instanciacion)
print (objeto2 == objeto1)
print(objeto2.distancia(objeto1))
print(objeto2.igualdad(objeto1))
