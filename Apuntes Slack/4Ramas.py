#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit

lArmas = ['katana', 'hacha', 'toalla mojada']
sEleccion = input('Un zombie ha asaltado tu casa, ¿con que te vas a defender? {0}> '.format(lArmas))
if sEleccion in lArmas:
    if 'toalla mojada' == sEleccion:
        print('Se escurre y se cae. Te salvas.')
    else:
        print('No esta afilada. ¡Has muerto!')
else:
    print('No existe esa arma. ¡Reza lo que sepas!')
