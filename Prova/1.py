with open("numeros.txt", "w") as n:
    for i in range(2, 101):
        if i % 2 == 0:
            n.write(f"{i}\n")
    n.close()