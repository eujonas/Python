"""12 - Esreva uma função que receba a medida do raio e calcule a 'área' e 'perímetro de uma circuferência'."""

def resultado(raio):
    area = 3.14 * (raio * raio)
    circuferencia = 2 * 3.14 * raio
    a = print("A área do círculo: %.2f" %area)
    c = print("A circuferência do círculo: %.2f" %circuferencia)
    return a,c

raio = float(input("Valor do raio:"))
x = resultado(raio) 
