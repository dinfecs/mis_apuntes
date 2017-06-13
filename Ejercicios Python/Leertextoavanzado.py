#Definimos ruta
ruta = 'libros.txt'
#leer contenido
contenido = open(ruta).read()
#Abrimos archivo
archivo = open(ruta, 'w')
#Pedimos nuevo texto
nuevo_texto = input('Dime tu nuevo libro favorito: ')
#Escribimos contenido
archivo.write(contenido + '\n' + nuevo_texto)
#Liberamos el archivo
archivo.close()
#informamos
print('Todo ha ido bien, no te pongas nervioso que me pongo nervioso yo y te reviento suhnormah')