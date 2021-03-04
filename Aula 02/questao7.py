"""7 - Escreva uma função que receba a idade do usuário e indique se ele pode ou não encher a cara de cachaça"""

def result(idade):
    if idade>=18:
        print("pode beber")
    else:
        print("nao pode, mas eu sim rsrs")
    return 

idade = int(input("qual sua idade?"))
x = result(idade) 

