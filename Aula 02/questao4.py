"""4 - Escreva uma função para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, a função deverá retornar quantos dias de vida um fumante perderá. Exiba o total em dias."""

def result(qntdia, qntanos):
    valorconvertido = qntdia*(10/1440) 
    diasPerdidos = valorconvertido*365*qntanos
    return diasPerdidos

qntdia= int(input("Quantos cigarros você fuma ao dia?:"))
qntanos =int(input("Há quantos anos você fuma?:"))
a = result(qntdia,qntanos)
print ("você perdeu %d dias da sua vida" %a)

