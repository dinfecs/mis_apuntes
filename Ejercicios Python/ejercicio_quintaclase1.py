alumnos = {
    'Marco': 6,
    'Chris': 4,
    'Estrella': 10,
    'Vero': 9.5,
    'Sara': 9.5,
    'Marc': 2.1
}
play = True

while play:
    print('+-------------+-------------+')
    print('|    Alumno   |   Nota      |')

    for alumno, nota in alumnos.items():
        print('+-------------+-------------+')
        print(f'|{alumno}     |{round(float(nota))}          |')
    print('+-------------+-------------+')
    opcion = input('1. Modificar \n'
                   '2. Nuevo\n'
                   '3. Borrar\n'
                   '4. Salir\n'
                   'INTRODUCE OPCIÓN: ')
    if opcion == '1':
        alumno_mod = input('Nombre: ')
        if alumno_mod in alumnos:
            nota_mod = input('Nota: ')
            alumnos[alumno_mod] = float(nota_mod)
        else:
            print('''
            Eso no existe, no te inventes nombres que me pones nervioso
            y te reviento la cabeza con el bordillo de la pared ELIGE UNO
            EXISTENTE MELÓN''')

    elif opcion == '2':
        alumno_nuevo = input('Nombre: ')
        nota_nueva = input('Nota: ')
        alumnos[alumno_nuevo] = nota_nueva

    elif opcion == '3':
        alumno_borrar = input('Nombre: ')
        del(alumnos[alumno_borrar])

    elif opcion == '4':
        play = False
        print('Pos na muchacho, enga ta luego payo.')