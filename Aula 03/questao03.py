"""3 - Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200 km, e R$ 0.45 para viagens mais longas."""

def result(distancia):
    if distancia<=200:
        acres = distancia * 0.50
        print(f"o preco da passagem fica {acres}")
    elif distancia>200:
        acres = distancia * 0.45
        print(f"o preco da passagem fica {acres}")
    
distancia = float(input("qual a distancia ate sua cidade?"))
x = result(distancia)
