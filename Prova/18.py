"""18 - Em campeonato de futebol por pontos corridos, as pontuações funcionam da
seguinte forma: 0 pontos por derrota, 1 ponto por empate e 3 pontos por vitória.
Construa uma função que receba a quantidade de vitórias, derrotas e empates de
um time e retorne a sua pontuação total ao fim do campeonato"""


def pontuacao(d,e,v):
    return (d*0) + (e*1) + (v*3)

d = int(input("numero de derrotas no campeonato:"))
e = int(input("numero de empates no campeonato:"))
v = int(input("numero de vitorias no campeonato:"))

x = pontuacao(d,e,v)
print("pontuacao ao fim do campeonato:",x)
