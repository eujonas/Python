"""13 - Crie uma função que resolva a seguinte equação do segundo grau X² + 3x +3 = 0. Dica para calcular a raiz quadrada -> num ** 0.5"""

def raizes(a, b, c):
    Delta = (b**2 - 4*a*c)
    x1 = (-b + Delta**(0.5)) / (2*a)
    x2 = (-b - Delta**(0.5)) / (2*a)
    print("\nX1: ", x1)
    print("X2: ", x2)
    return
raizes(1,3,3)
