#Variables
tareas = ['Falsa', 'mentira']
for num, item in enumerate(tareas, 1):
    print('{num}. {item}'.format(num=num, item=item))

play = True
#tareas
print('BIENVENIDO A TU LISTA DE TAREAS V0.1')
while play:
    print('\n' * 100)
    print('____________________________')
    #imprimir tareas
    for tarea in tareas:
        print('- {tarea}'.format(tarea=tarea))
    print('____________________________')
    #lista de opciones
    print('1. Nueva')
    print('2. Modificar')
    print('3. Eliminar')
    print('4. Salir')

    #opcion
    opcion = int(input('Seleciona la acción que deseas realizar: '))

    if opcion == 1:
        # opcion añadir
        nueva_tarea = input('Escribela: ')
        tareas.append(nueva_tarea)
    elif opcion == 2:
        # modificar tarea
        tarea_mod = input('Dime el nuevo texto: ')
        pos_mod = int(input('¿Qué posición deseas modificar?'))
        tareas[pos_mod] = tarea_mod
    if opcion == 3:
        #eliminar tarea
        pos_eli = int(input('Escribe el numero de tarea: '))
        tareas.pop(pos_eli)
    elif opcion == 4:
        play = False
print('Hasta luegui.')

