"""6 - Utilizando while imprima os resultados da tabuada de 2:
A saída deve ser semelhante a:
2 x 1 = 2
2 x 2 = 4
"""
n1 = 2
cont = 1
while (cont < 11):
    tab = n1 * cont
    print('{} x {:2} = {}'.format(n1,cont,tab))
    cont += 1
