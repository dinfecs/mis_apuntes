# Bibliotecas
import random

# Variables
baraja = [1, 2, 3, 4, 5, 6, 7, 0.5, 0.5, 0.5]
mano = []
play = True

# Funciones
def limpiar():
    for i in range(100):
        print('\n')

def imprimir_mano(mano):
    '''
    Imprime la mano
    :param mano:
    '''
    final = ''
    # Recorremos la mano
    for carta in mano:
        # Concadenamos con un espacio cada uno de los elementos
        final += str(carta) + ' '
    # Imprimimos el resultado
    print(final)

while play:
    opcion = int(input('1) Carta 2) Plantarse: '))
    if opcion == 1:
        pos_random = random.randint(0, len(baraja) - 1)
        carta = baraja.pop(pos_random)
        limpiar()
        print('Te ha salido ' + str(carta))
        mano.append(carta)
        imprimir_mano(mano)
        print('Tu mano es : ' + str(mano))
        #comprobar si termino el juego
        suma = 0
        for carta in mano:
            suma += carta
        print('Tienes un total de: ' + str(suma))
        if suma == 7.5:
            print('Has ganado')
            play = False
        elif suma > 7.5:
            print('Has perdido')
            play = False

    elif opcion == 2:
        play = False

print('Game over')