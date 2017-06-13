#!/usr/bin/env python
# -*- coding: utf-8 -*-

lVacia1 = []
lVacia2 = list()
lPrendas = ['camiseta', 'vestido', 'zapato', 'pantalón']
lTallas = [10, 20, 30, 40, 50, 60]
lStocks = ['Ninguno', 1, 2, 3, 'Varios']

print('%d -----------' % 1)
print(lPrendas[1])
print(lTallas[0])
print(lPrendas[1:4]) #Simir a range
print(len(lStocks))
print(lPrendas[-1])

print('%d -----------' % 2)
lPrendas.append('Sombreros') #Añade a la lista
print(lPrendas)

print('%d -----------' % 3)
lPrendas.append('zapato') 
iNumZapatos = lPrendas.count('zapato') #Busca y cuenta
print('Hay %d zapatos' % iNumZapatos)

print('%d -----------' % 4)
lPrendas.insert(0, 'guantes') #Inserta en una posición 
print(lPrendas)

print('%d -----------' % 5)
lPrendas.remove('camiseta') #Elimina un valor
print(lPrendas)

print('%d -----------' % 6)
print(lPrendas.pop())#Elimina el último y lo devuelve. A no ser que indiques la posicion que quieras Ejem: pop(2)
print(lPrendas)

print('%d -----------' % 7)
lPrendas.reverse() #Da la vuelta
print(lPrendas)

print('%d -----------' % 8)
sPalabras = 'No me separes mala persona'
lPalabras = sPalabras.split(' ') #Convierte en una lista separando por el argumento
print(lPalabras)

print('%d -----------' % 9)
sPalabras = 'No me separes mala persona'
lPalabras = sPalabras.split(' ') 
print(' - '.join(lPalabras)) #Concadena una cadena con una lista, devolviendo un string
