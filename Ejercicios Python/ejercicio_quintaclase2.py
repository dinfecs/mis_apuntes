
class Alumno(object):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.pagado = False

    def mayor_edad(self):
        if self.edad >= 18:
            print('es mayor')
        else:
            print('es menor')

mi_marco = Alumno('Marco', 20)
mi_marco.mayor_edad()

mi_vero = Alumno('Vero', 11)
mi_vero.mayor_edad()