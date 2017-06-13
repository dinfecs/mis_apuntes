from datetime import datetime
#Mensaje de bienvenida
print('''
    CHACHINGPIRULING v0.1
''')
anyo_nacimiento = int(input('Ingresa tu año de nacimiento '))
EDAD_LIMITE = 18
anyo_actual = datetime.now().year

if anyo_actual - anyo_nacimiento >= EDAD_LIMITE:
    print('Puedes pasar')
else:
    print('YOU SHALL NOT PASS')