from sys import argv #Se necesita importar argv para obtener los parámetros
from os.path import exists #Se necesit para averiguar si existe el archivo

script, rutaTXT = argv

archivoTXT = open(rutaTXT)
contenidoTXT = archivoTXT.read()
print("Existe? %r" % exists(rutaTXT))
print("El archivo pesa %d bytes" % len(contenidoTXT))

archivoTXT.close()
