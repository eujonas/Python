"""1 - Escreva uma função que simule o funcionamento de um radar eletrônico. Essa função deve receber a velocidade do carro de um usuário. Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 90 reais pela infração + R$ 5 reais por km acima de 80 km/h"""

def result(velocidade):
    if velocidade>80:
        multa = (velocidade - 80) * 5
        print(f"voce foi multado em R${multa}")
    else:
        print("continue...")
    return

velocidade = int(input("qual sua velocidade?"))
x = result(velocidade)




