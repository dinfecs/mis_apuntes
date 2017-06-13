# Variables
rutaTXT = 'tareas.txt'
tarea = input("Tarea:\n")

# Obtenemos las tareas del documento
archivoTXT = open(rutaTXT)
contenidoActual = archivoTXT.read()

# Concadenamos el texto del archivo con la tarea y un salto de linea
textoCompleto = contenidoActual + tarea + '\n'

# Escribimos todo en el documento
archivoTXT = open(rutaTXT, 'w')
archivoTXT.write(textoCompleto)
archivoTXT.close()

# Nos despedimos
print('Que pase un buen dia')