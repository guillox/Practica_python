"""
12.-Modelice con objetos a los alumnos y materias de la facultad. Un alumno debe tener como
información mínima el nombre y apellido, número de legajo y fecha de nacimiento. Implemente
un método para asignarle materias que esté cursando el alumno y aquellas que aprobó junto
con su nota. Implemente un método que calcule el promedio de todas las cursadas que aprobó
un alumno y luego realice un listado de aquellos alumnos que estén cursando al menos 2
materias.
A continuación se verá el diagrama UML asociado:
lista=["hola","chau","casa

crear getmateriaaprobas
"""



class Materia:
    def __init__(self, nombre, anio):
        """
        :param nombre:
        :param año:
        """
        self.__nombre = nombre
        self.__anio = anio

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getAnio(self):
        return self.__anio

    def setAnio(self, anio):
        self.__anio = anio


class MateriaAprobada():
    def __init__(self, materia, nota):
        self.__materia = materia
        self.__nota = nota

    def getMateria(self):
        return self.__materia

    def setMateria(self, materia):
        self.__materia = materia

    def getNota(self):
        return self.__nota

    def setNota(self, nota):
        self.__nota = nota


class Alumno():
    """docstring for alumno"""


    def __init__(self, nombre, apellido, legajo, fechadenacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__legajo = legajo
        self.__fechadenacimiento = fechadenacimiento
        self.__materiaaprobadas = []
        self.__cursadas = []

    def getnombre(self):
        return self.__nombre

    def getapellido(self):
        return self.__apellido

    def getlegajo(self):
        return self.__legajo

    def getfechadenacimiento(self):
        return self.__fechadenacimiento

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setapellido(self, apellido):
        self.__apellido = apellido

    def setlegajo(self, legajo):
        self.__legajo = legajo

    def setfechanacimiento(self, fechanacimiento):
        self.__fechadenacimiento = fechanacimiento

    def AgregarMateria(self,materias):
        self.__materiaaprobadas.append(materias)

    def getPromedioAprobadas(self):

        if len(self.__materiaaprobadas) == 0:
            return 0
        else:
            suma = 0
            for materia in self.__materiaaprobadas:
                suma += materia.getNota()
            return suma / len(self.__materiaaprobadas)



alumno1 = Alumno('jose', 'marti', 1234, 12345)
cursada = Materia("mate2", 2)
mateAprob = MateriaAprobada(cursada, 9)
alumno1.AgregarMateria(mateAprob)
cursada = Materia("mate3", 2)
mateAprob = MateriaAprobada(cursada, 4)
alumno1.AgregarMateria(mateAprob)
print(alumno1.getPromedioAprobadas())














