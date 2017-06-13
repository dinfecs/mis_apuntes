print('hola mundo')

perro = 4
gato = 'bigotes'
existe = True
perro2= 6

print(perro + perro2)

paco, manolo, juan = 1, 2, 3

num_1, num_2 = 6, 9

num_total = num_1 + num_2

print(num_total)

num_3, num_4 = 'hola', 'mundo'

num_total2 = num_3 + num_4

print(num_total2)
#forma1
texto = 'me gusta conducir en'
ciudad = 'Valencia'

final = texto + ciudad

print(final)

#Forma2
texto2 = 'El limite de %s es de %d Km/h' % ('volar', 120)
print(final + texto2)

#forma3
texto3 = 'El circo del {nombre_circo}, estará hasta {fecha}' .format(nombre_circo='sol', fecha='Diciembre')
print(texto3)

#forma4
regalo = 'osito'
texto4 = f'me han regalado un {regalo}'
print(texto4)

#bloques

texto5 = '''
    Esternocleidomastoideo
    Esternocleidomastoideo
    Esternocleidomastoideo
    Esternocleidomastoideo
'''

comida1 = 'panes'
comida2 = 'peces'

print(comida1 * 100)
print('peces' * 100)