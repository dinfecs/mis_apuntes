class Tweet(object):

    def __init__(self, text):
        self.like = 0
        self.text = text
    def aumentar_like(self):
        self.like += 1

LIMIT = 140
list_tweets = [Tweet('@Cosita Me encanta.'), Tweet('@Ayquemequedo Me voy.')]
play = True
error = False
buscar = False
buscar_palabra =''
mensaje_error = ''

while play:
    print('-------------------------')
    print('---------TWITTER---------')
    print('-------------------------')
    for pos, tweet in enumerate(list_tweets):
        if (buscar and tweet.text.find(buscar_palabra) >= 0) or not buscar:
            print(f'\u2605{tweet.like}\n'
                f'{pos}. 'f'{tweet.text}''\n'
                '-------------------------')
    print('1. Nuevo')
    print('2. Like')
    print('3. Buscar')
    print('4. Salir')
    if error:
        print('')
        print(mensaje_error)
        print('')
        error = False
    opcion = input('Introduce opción: ')

    if opcion == '1':
        texto = input('Introduce Tweet: ')
        if len(texto) <= LIMIT:
            list_tweets.append(Tweet(texto))
        else:
            mensaje_error = f'No Puedes añadir mas de {LIMIT} caracteres'
            error = True

    elif opcion == '2':
        pos_like = int(input('Posicion: '))
        list_tweets[pos_like].aumentar_like()

    elif opcion == '3':
        buscar_search = input('Buscar: ')
        buscar = True

    elif opcion == '4':
        play = False