def imprimir_nombre():
    '''
    Funcion para imprimir nombre
    '''
    print('Soy manolo')
#ejecutar función
imprimir_nombre()

def poner_mayusculas(texto):
    print(texto.upper())

poner_mayusculas('me gusta')

def poner_mayusculas2(texto,texto2):
    print(texto.upper() + texto2)

def multiple(*texto):
    print(len(texto))
    print(texto[1])

multiple('rato', 'largo', 'avion')

def sumar(num1, num2):
    return num1 + num2

total = sumar(5 , 7)

print(total)