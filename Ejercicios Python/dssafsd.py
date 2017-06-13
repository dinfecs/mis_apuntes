nombre = input('Tu nombre: ')
sexo = input('Genero: ')
hijos = int(input('Numero de hijos: '))

textofinal = ''

if sexo == 'hombre':
    textofinal = textofinal + 'El señor '
elif sexo == 'mujer':
    textofinal = textofinal + 'la señora'

textofinal = textofinal + nombre
if hijos == 0:
    textofinal = textofinal + 'no tiene '
else:
    textofinal = textofinal + ' tiene ' + str(hijos) + ' hijos.'

print(textofinal)
