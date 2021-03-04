"""8 - P = True e Q = False. Aplique De Morgan na seguinte proposição e atribua o valor a uma variável - ~(p ^ (p v q)), essa variável deve ser retornada partir de uma função"""

def result(P,Q):
    resposta = not P or(not P and not Q)
    return resposta
x = result(True,False) 
print(x)


