#!/usr/bin/env python
# -*- coding: utf-8 -*-

dJamesBond = {
        'Sean Connery': 'Dr. No, From Russia With Love, Goldfinger, Thunderball',
        'David Niven': 'Casino Royale',
        'George Lazenby': 'On Her Majesty Secret Service',
        'Roger Moore': 'Live and Let Die, The Man with the Golden Gun'
        }
#Leer
print(dJamesBond['David Niven'])

#Modificar
dJamesBond['David Niven'] = 'Octopusy'
print(dJamesBond['David Niven'])

#Anyadir
dJamesBond[4] = {'Sean Connery': 'Dr. No, From Russia With Love, Goldfinger, Thunderball'}

#Borrar
del dJamesBond['David Niven']
print(dJamesBond)

#Solo keys
print(dJamesBond.keys())

#Buscar key
if 'Roger Moore' in dJamesBond:
    print('Encontrado!')

#Recorrer keys
for peliculas in dJamesBond:
    print('Peli: %s' % peliculas)

#Recorrer values
for actor, peliculas in dJamesBond.items():
    print('El actor %s trabajó en %s' % (actor, peliculas))
