Num1 = float(input('Precio sin iva'))
precio_iva = Num1 * 0.21
resultado = precio_iva + Num1
print('''
    Precio sin iva: {Num1}
    IVA: {precio_iva}
    Total a pagar: {resultado}
    '''.format(resultado=resultado, Num1=Num1, precio_iva=precio_iva))