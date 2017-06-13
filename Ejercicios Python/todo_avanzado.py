# TODO


class Tarea(object):

    def __init__(self, texto, prioridad):
        self.texto = texto
        self.prioridad = prioridad
        self.equivalencias = ['Alta', 'Media', 'Baja']

    def texto_prioridad(self):
        return self.equivalencias[self.prioridad - 1]

list_tareas = [Tarea('fregar', 3), Tarea('pagar recibo', 1)]

play = True

while play:

    for item in list_tareas:
        print(f'"{item.texto}"({item.texto_prioridad()})')

    texto_nuevo= input('Añade nueva tarea: ')
    prioridad_nuevo= int(input('Prioridad (1, 2, 3): '))
    if pri
    list_tareas.append(Tarea(texto_nuevo, prioridad_nuevo))