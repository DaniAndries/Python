import random
contador = int(0)
aleatorio = int(0)
while aleatorio != 5:
    aleatorio = random.randint(1, 6)
    print(aleatorio)
    contador = contador+1
print("Se ha lanzado", contador, "veces")
