"""11- Escreva um programa que receba as medidas dos lados de um triângulo e calcule sua área e perímetro."""


"""       .
         . .
     A  .   .  B
       . . . .
          C

"""
import math

ladoa = int(input("Lado A do triangulo:"))
ladob = int(input("Lado B do triangulo:"))
base = int(input("Base do triangulo:"))
         
perimetro  = ladoa * ladob * base
print("perimetro:", perimetro )

x = input("LadoA ou LadoB?")
if x == "LadoA":
    result = (base ** 2 + ladoa ** 2) ** (1/2)
    "result = math.hypot(base,ladoa)" 
    area = (base * result) / 2
    print("area: %.2f" %area)
elif x == "LadoB":
    result = (base ** 2 + ladob ** 2) ** (1/2)
    "result = math.hypot(base,ladob)" 
    area = (base * result) / 2
    print("area: %.2f" %area)



     
    