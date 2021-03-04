"""9 - Crie uma função que receba duas strings e retorne True se o número de elementos de uma for igual ao da outra, e retorne False caso contrário.Pesquise pelo método len() na documentação do Python."""

def result(palavra1,palavra2):
    if len(palavra1) == len(palavra2):
        print("verdadeiro")
    else:
        print("false")
    return 
palavra1 = input("primeira palavra: ")
palavra2 = input("segunda palavra: ")
x = result(palavra1,palavra2) 

