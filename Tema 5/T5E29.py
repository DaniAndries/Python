numero1 = int(input())
numero2 = int(input())
contador = 0
for i in range(numero1, numero2 + 1):
    if i % 2 == 0:
        contador = contador + 1
    print(" ")
print("Han habido ", contador, " pares")
