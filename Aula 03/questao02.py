"""2 - Faça uma função que receba como argumento o salário de um funcionário e calcule o valor do aumento com base nos dados abaixo. Para salários superiores a R$ 1.250,00 Reais, calcule um aumento de 10%. Para os inferiores ou iguais, 15% de aumento."""

def salario(valor):
    if valor>1250:
        acres = valor + (valor*0.10)
        print(f"seu salario com o acrescimento fica {acres}")
    elif valor<=1250:
        acres = valor + (valor*0.15)
        print(f"seu salario com o acrescimento fica {acres}")
    return
valor = int(input("qual o seu salario?"))
x = salario(valor)

