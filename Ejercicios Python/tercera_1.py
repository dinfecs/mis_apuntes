num = 0
for i in range(0, 201, 2):
    texto = '2 X {numeral} = {resultado}'.format(numeral=num, resultado=i)
    print(texto)
    num += 1