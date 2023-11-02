suma = int(0)
for i in range(0, 15):
    numero = int(input())
    suma = suma + numero
    if numero > 1000:
        break
print(suma)