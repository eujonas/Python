"""13 - Faça um programa para escrever a contagem regressiva do lançamento de um
foguete. O programa deve imprimir 10, 9, 8..., 1, 0 e "Fogo!". Detalhe, o cronômetro
está quebrado e pula os números pares."""

impares = []
for contagem in range(10, -1, -1):
    if contagem % 2 != 0:
        impares.append(contagem)
print(impares)
print("FOGO!")



