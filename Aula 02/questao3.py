"""3-Crie uma função que retorne o resto da divisão do resultado da função da questão anterior por 2"""

num1 = int(input("Primeiro valor:"))
num2 = int(input("Segundo valor:"))

def result(num1, num2):
    return (2 * num1) *(3 * num2)

a = result(num1, num2) 
resto = a % 2
print(resto)
