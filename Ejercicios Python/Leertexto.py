#Definimos ruta
ruta = 'libros.txt'
#Abrimos archivo
archivo = open(ruta)
#Leemos archivo
texto_archivo = archivo.read()
#Imprimimos
print(texto_archivo.upper())