"""8 - Faça uma função que receba uma lista de números inteiros e retorne o maior elemento desta lista. Utilize o for"""
 
lista = []
def criar(lista):
    for i in range(0, 3):
        lista.append(int(input(f"digite um valor para prosição {i}:")))

    print ("O maior elemento: ", max(lista))
x = criar(lista)