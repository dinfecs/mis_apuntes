#!/usr/bin/env python
# -*- coding: utf-8 -*-

iNumPersonas = 20
iNumGatos = 30
iNumPerros = 15


if iNumPersonas < iNumGatos:
    print("Los gatos han conquistado el mundo. ¡Larga vida a nuestro amos!")

if iNumPersonas > iNumGatos:
    print("Hemos ganado la guerra gatuna. ¡El mundo esta a salvo!")

if iNumPersonas < iNumPerros:
    print("Pronto no quedarán bolsitas para recoger las caquitas.")

if iNumPersonas > iNumPerros:
    print("¿Quién ha sido un chico bueno?")

iNumPerros += 5

if iNumPersonas >= iNumPerros:
    print("Un perro una persona o más personas. No todos podemos tener una mascota.")

if iNumPersonas <= iNumPerros:
    print("Hay igual o menos personas que perros. Es hora de hacer comida china.")


if iNumPersonas == iNumPerros:
    print("Por igual. Ha desaparecido la soledad.")
