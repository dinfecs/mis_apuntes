#Definimos ruta
ruta = 'libros.txt'
archivo = open(ruta)

texto = archivo.read()
#primeralinea
#print(archivo.readline())
print(texto)