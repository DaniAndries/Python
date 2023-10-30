mayor = -9999
menor = 9999
cantidad = int(input())
suma = 0
for i in range(0, cantidad):
    numero = int(input())
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    suma = suma + numero
media = suma / cantidad
print("Mayor: ", mayor, "Menor: ", menor, "Media: ", media)
