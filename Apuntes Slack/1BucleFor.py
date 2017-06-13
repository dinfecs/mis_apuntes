#!/usr/bin/env python
# -*- coding: utf-8 -*-

lPrendas = ['camiseta', 'vestido', 'zapato', 'pantalón']

for sItem in lPrendas:
    print("%s esta en la lista" % sItem)

print("--- Primero 7 elementos ---")
for i in range(7):
    print("Número %d" % i)

print("--- Rango del 4 al 7 ---")
for i in range(4, 7):
    print("Número %d" % i)

print("--- Tabla del 4 ---")
for i in range(0, 41, 4):
    print(i)

print("--- Generar lista ---")
lVersionesAdobe = []
for i in range(1, 7):
   lVersionesAdobe.append("CS" + str(i)) 
print(lVersionesAdobe)


for i, v in enumerate(lPrendas):
    print('%d: %s' % (i, v))
