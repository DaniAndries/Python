numero = int(input())
while numero < 0 & numero > 20:
    print("Numero inválido")
    numero = int(input())
for i in range (0, numero):
    for j in range (0, i):
        print(i, end=" ")
    print("")