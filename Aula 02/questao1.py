"""1 - Converta as seguintes expressões matemáticas para que possam ser calculadas usando Python:
10 + 20 x 30
4² / 3
(9⁴ + 2) x 6 -1
(9⁴ + 2)⁴ + ( 10 / 1)
"""

a = float(10 + (20 * 30))
b = float(4 ** 2 ) / 3
c = float(9 ** 4 + 2) * (6-1)
d = float((9 ** 4 + 2) ** 4) + (10/1)

print("%.2f"%a)
print("%.2f"%b)
print("%.2f"%c)
print("%.2f"%d)