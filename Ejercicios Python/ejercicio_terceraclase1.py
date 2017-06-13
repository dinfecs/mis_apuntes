armas = ('pistola', 'cuchillo', 'impuestos')

texto_armas = ' '.join(armas)

texto_inicio = 'Selecciona un arma: {armas} '.format(armas=texto_armas)

opcion = input(texto_inicio)

if opcion in armas:
    if opcion == armas[-1]:
        print('Le has enviado una carta falsa de hacienda y le ha dado un paro cardiaco.')
else:
    print('Te has resbalado y te has dado con el filo de la mesita de noche. ¡HAS MUERTO!')