numero = int(input())
contador = 0
while numero != 0:
    digito = int(numero % 10)
    print(digito, end=" ")
    numero = int(numero / 10)
    contador = contador + 1
print("")
print("Hay", contador, "dígitos")
