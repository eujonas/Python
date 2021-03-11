"""12 - Escreva um programa que pergunte a distância que um passageiro deseja
percorrer em km. Calcule o preço da passagem, cobrando R $0.05 por metro para
viagens de até 200 km, e R $0.10 para viagens mais longas."""


distancia = float(input("qual a distancia?"))
if distancia <= 200:
    preco = (distancia * 1000) * 0.05
    print(f"preco da passagem:R${preco}")
elif distancia >200:
    preco = (distancia * 1000) * 0.10
    print(f"preco da passagem:R${preco}")
