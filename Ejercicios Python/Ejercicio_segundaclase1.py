ruta = 'libros.txt'
contenido = open(ruta).read()
archivo = open(ruta, 'w')
pedir_tarea = input('Añade tarea: ')
pedir_tarea2 = input('Añade tarea: ')
pedir_tarea3 = input('Añade tarea: ')
archivo.write(contenido + '\n' + pedir_tarea)
archivo.close()
print('''
    Bienvenido al gestor de tareas CHACHINGPISTACHING v0.1

    Esta es la lista de tus tareas:

    1- {pedir_tarea}

    2- {pedir_tarea2}

    3- {pedir_tarea3}

    Has ordenado tu lista de tareas con éxito, no te pongas nervioso que me pones nervioso a mi y te reviento la vida
'''.format(pedir_tarea=pedir_tarea, pedir_tarea2=pedir_tarea2, pedir_tarea3=pedir_tarea3))