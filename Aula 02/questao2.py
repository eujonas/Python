"""2-Escreva uma função que receba dois números como argumento e retorne o produto do dobro do primeiro pelo triplo do segundo """

num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

def result(num1, num2):
    return (2 * num1) *(3 * num2)

a = result(num1, num2)   # retornar
print(a) # função imprimir o valor
