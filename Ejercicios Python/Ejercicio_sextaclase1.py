import random

#Ahorcado v0.1

lista_palabras = ['habitacion', 'telesilla', 'avion', 'enano', 'circo']
intentos = 5
play = True
ganar = False

solucion_palabra = lista_palabras[random.randint(0, len(lista_palabras) - 1)]
list_solucion = []
for pos in range(len(solucion_palabra)):
    list_solucion.append('_')

while play:
    print('\n' * 100)
    print(' '.join(list_solucion))
    print(f'Tienes {intentos} intentos.')

    letra = input('Dame una letra: ')

    if len(letra) > 1:
        print('Solo puedes escribir una letra a la vez')
    else:
        if letra in solucion_palabra:
            for index, letra_solucion in enumerate(solucion_palabra):
                if letra == letra_solucion:
                    list_solucion[index] = letra
        else:
            intentos -= 1

    if intentos == 0:
        play = False
        print('\n' * 100)
        print('Has perdido')
    elif ''.join(list_solucion) == ''.join(solucion_palabra):
        play = False
        print('\n' * 100)
        print('Has ganado')
print(f'La solución es: {"".join(solucion_palabra)}')