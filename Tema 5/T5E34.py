numero = int(input())
contador = 0
while numero != 0:
    digito = int(numero % 10)
    print(digito)
    numero = int(numero / 10)
    contador = contador + 1
print("Hay", contador, "dígitos")
