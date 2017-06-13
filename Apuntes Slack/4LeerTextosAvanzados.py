from sys import argv

script, rutaTXT = argv

archivoTXT = open(rutaTXT)

# Método que imprime todo el contenido del archivo
print(archivoTXT.read())

# Método que cambia la posición de lectura del archivo
iniPos = 4
archivoTXT.seek(iniPos)
print(archivoTXT.read())

# Método que vuelve al principio del archivo
archivoTXT.seek(0)

# Método que lee e imprime una línea 
print(archivoTXT.readline())
