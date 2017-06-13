from sys import argv # Se necesita importar argv para obtener los parámetros

script, rutaTXT = argv
archivoTXT = open(rutaTXT)
contenidoTXT = archivoTXT.read()

print("%s" % contenidoTXT)
