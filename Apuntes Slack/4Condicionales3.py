#!/usr/bin/env python
# -*- coding: utf-8 -*-

iEdad = 20 
iAdulto = 18
iAnciano = 65

if iEdad >= iAdulto and iEdad < iAnciano:
    print("Soy de mediana edad.")

if iEdad == iAnciano or iEdad == iAdulto:
    print("Hoy es un día importante para ti.")


def isMenorDeEdad(iniEdad):
    """Devuelve si es menor de edad.
    
    Parámetros de entrada:
    iniEdad -- Edad
    """
    bMenor = True
    if iniEdad >= 18:
        bMenor = False
    return bMenor

if isMenorDeEdad(iEdad):
    print("Soy menor de edad.")
