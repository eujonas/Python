"""14 - Um fazendeiro cria Galinhas, Vacas e Porcos. Escreva uma função que receba a quantidade de cada animal que o fazendeiro possui atualmente e retorne quantas patas tem na fazenda"""

g = int(input("Número de galinhas:"))
v = int(input("Número de vacas:"))
p = int(input("Número de porcos:"))

def resultado(g,v,p):
    galinhas = 2 * g
    vacas = 4 * v
    porcos = 4 * p
    soma = galinhas + vacas + porcos
    return soma

a = resultado(g,v,p)
print("existem %d patas na fazenda" %a)
