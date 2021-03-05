"""10 - Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo(8min15s por quilômetro), então 3 quilômetros a uma passo mais rápido(7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?"""


#total = (15 + 12*3 + 15) + ((52 + 8 + 7*3 + 8) * 60) + (6 * 60 * 60)
total = 27006 #em segundos

seg = (total % 60) % 60
minutos = (total // 60) % 60
horas = (total // 60) // 60

print(f"voce chegara as {horas}:{minutos}:{seg}")

