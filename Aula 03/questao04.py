"""4 - Escreva uma função para aprovar o empréstimo bancário para compra de uma casa. Essa função deve receber o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar"""

def emprestimo(valor_casa, salario, qnt_anos):
    prestacao = valor_casa / (qnt_anos*12)
    if prestacao>(salario*0.30):
        print("o valor da prestacao ultrapassa 30%' do seu salario")
    else:
        print("EMPRESTIMO APROVADO. \nTotal mensal: R$%.2f"%prestacao)
        
valor_casa = float(input("qual o valor da casa:"))
salario = float(input("qual o seu salario:"))
qnt_anos = int(input("quantos anos pretende pagar:"))
x = emprestimo(valor_casa,salario,qnt_anos)
