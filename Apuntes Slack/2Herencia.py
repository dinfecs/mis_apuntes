#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Padre
class Persona(object):

    def __init__(self, insNombre):
        self.sNombre = insNombre 

    def saludar(self):
        print('Hola soy una persona.')

# Hijo
class Pareja(Persona):

    def __init__(self, insMote):
        self.sMote = insMote

    def saludar(self):
        print('Hola soy una novia.')


# Hijo
class Familia(Persona):

    def __init__(self, insParentesco):
        self.sParentesco = insParentesco
    
    def saludar(self):
        print('Hola soy un familiar.')

    def saludarComoPersona(self):
        super(Familia, self).saludar()


miNovia = Pareja('Cari')
miNovia.sNombre = 'Luisa'
miAbuelo = Familia('Paterno')
miAbuelo.sNombre = 'Antonio'

print('-' * 20 + ' Novia ' + '-' * 20)
print('Nombre: %s' % miNovia.sNombre)
print('Mote: %s' % miNovia.sMote)
miNovia.saludar()
print('-' * 20 + ' Abuelo ' + '-' * 20)
print('Nombre: %s' % miAbuelo.sNombre)
print('Parentesco: %s' % miAbuelo.sParentesco)
miAbuelo.saludar()
miAbuelo.saludarComoPersona()
