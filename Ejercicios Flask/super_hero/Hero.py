class Heroe(object):

    def __init__(self, nombre, descripcion, sexo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.sexo = sexo
        self.sexo_nombres = ('Mujer', 'Hombre')

    def get_sexo(self):
        return self.sexo_nombres[self.sexo - 1]