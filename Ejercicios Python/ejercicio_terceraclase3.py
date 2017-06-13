import random
print('Bienvenido a la cueva del Golum. ¡MI TESO~RO!')

oportunidades = 3
respuesta = random.randint(0, 10)

play = True
while play:
    mensaje = int(input('Dime un numero entre el 1 y el 10: '))

    if mensaje == respuesta:
        play = False
        print('¡OH~! ¡Has ganado!')
    else:
        oportunidades -= 1
        print('Has fallado. Te quedan {oportunidades}'.format(oportunidades=oportunidades))
    if oportunidades ==  0:
        play = False
        print('GAME OVER')