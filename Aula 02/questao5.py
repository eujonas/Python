"""5- Escreva uma função que receba como argumento a quantidade de Km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. A função deve retornar o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado."""
 
def valor(km, dia):
    gastos = (60 * dia) + (0.15 * km) 
    return gastos

km = int(input("Quantidade de Km percorrido:"))
dia = int(input("Quandidade de dias alugado:"))

a = valor(km,dia)
print("Preço a pagar R$", a)