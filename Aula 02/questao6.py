"""6 - Suponha que o preço de capa de um livro seja 24.95. mas as livrarias recebem um desconto de 40%. O transporte custa 3.00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 copias?"""

desconto = (24.95*0.40)
capa = 24.95- desconto
transporte1 = 3
transporteAdd = 0.75 * 59

total = capa + transporte1 + transporteAdd
print("total no atacado R$:", total)
