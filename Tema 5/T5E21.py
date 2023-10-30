numero = int(input())
contador = 0
for i in range(1, numero):
    if numero % i == 0:
        contador = contador + 1
if contador > 2:
    print("No es primo")
else:
    print("Es primo")
