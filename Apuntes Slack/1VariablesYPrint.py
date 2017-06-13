# -*- coding: utf-8 -*-

#Soy un comentario
sNombre = 'Andros'
sApellido = 'Fenollosa'
iEdad = 28
bUtilSocidad = False

# Forma 1
print('Me llamo el condeduque %s de Valencia alta' % sNombre) #Concadenar String
print('y tengo %d años' % iEdad) #Concadenar entero
print('En serio, me llamo %s y tengo %d años' % (sNombre, iEdad)) #Concadenar varios
print('RAW %r' % sApellido ) #Concadenar binario

# Forma 2
print('Soy otra forma de concadenar ' + sNombre + ' ' + sApellido) #Concadeno moderno

# Forma 3
texto = 'Soy la {0}a forma de concadenar'.format(3)
print(texto)

texto = 'Soy la {0}a forma de concadenar {1}'.format(3, 'Aviones')
print(texto)


print('.' * 10) #Repetir string

print('''
        Soy un bloque de texto.
        Y soy libre para que pongas
        lo que quieras.
''')

print('Voy a desaparecer\r ¿ves?') #Retorno de carro
