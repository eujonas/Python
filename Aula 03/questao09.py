"""9 - Gere as seguintes listas utilizando for e o metodo range():
Uma lista de ímpares de 10 a 12o
Uma lista pares de 2 a 1000
Uma lista de multiplos de 2 em um intervalo de decrescente de 100 até 40
Uma lista de primos de 44 até 99
OBS: Pesquise pelo método append() na documentação """

#IMPARES

impares = []
for i in range(10, 20):
    if i % 2 != 0:
        impares.append(i) 
print("IMPARES:",impares)

#PARES

pares = []
for i in range(2, 15):
    if i % 2 == 0:
        pares.append(i)
print("\nPARES:",pares)

#MULTIPLOS

multiplos = []
for i in range(1,60):
    if i % 7 == 0:
        multiplos.append(i)
multiplos.reverse() #reverse é utilizado para imprimir na ordem decrescente
print("\nMULTIPLOS:",multiplos)

#PRIMOS

primos = []
for x in range(1,25):
    cont=0
    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont <= 2:
            primos.append(x)

print("\nPRIMOS:",primos)



