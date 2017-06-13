from sys import argv #Se necesita importar argv para obtener los parámetros

script, rutaTXT = argv

sNuevoTexto = input("Dime que quieres escribir:\n")

archivoTXT = open(rutaTXT, 'w') #Permisos de escritura
archivoTXT.truncate() #Vacía el archivo
archivoTXT.write(sNuevoTexto)
archivoTXT.close()

#close -- Cierra el archivo. Similar a pulsar el botón de salvar
#read -- Lee el archivo
#readline -- Lee una lína
#truncate -- Vacía el archivo
#write('texto') -- Escribe
