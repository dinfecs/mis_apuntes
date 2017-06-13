#!/usr/bin/env python
# -*- coding: utf-8 -*-

def romperPorPalabras(insFrase):
    """Rompe una frase por palabras.
    
    Keyword arguments:
    insFrase -- Texto o frase
    """
    aPalabras = insFrase.split(' ')
    return aPalabras 

def ordenarPorLetras(insTexto):
    """Ordena las letras por orden alfabético.
    Ejemplo: 'Hola mundo' -> [' ', 'H', 'a', 'd', 'l', 'm', 'n', 'o', 'o', 'u']
    
    Keyword arguments:
    insTexto -- Texto
    """
    return sorted(insTexto)

def primeraPalabra(insTexto):
    """Obtiene la primera palabra de un texto.
    
    Keyword arguments:
    insTexto -- Texto
    """
    aPalabras = romperPorPalabras(insTexto)
    sPalabra = aPalabras.pop(0)
    return sPalabra

def ultimaPalabra(insTexto):
    """Obtiene la última palabra de un texto.
    
    Keyword arguments:
    insTexto -- Texto
    """
    aPalabras = romperPorPalabras(insTexto)
    sPalabra = aPalabras.pop(-1)
    return sPalabra

def ordenarPalabras(insTexto):
    """Ordena las palabras por orden alfabético.
    Ejemplo: 'Que es poesía te preguntas mientras clavas tu pupila' 
        -> ['Que', 'clavas', 'es', 'mientras', 'poesía', 'preguntas', 'pupila', 'te', 'tu']
    
    Keyword arguments:
    insTexto -- Texto
    """
    aPalabras = romperPorPalabras(insTexto)
    return sorted(aPalabras)
