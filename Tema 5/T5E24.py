numero1 = int(input())
contador = 0
for i in range(1, numero1):
    if i % 3 == 0:
        print(i, " es multiplo de 3")
    contador = contador + 1
print("Han habido ", contador, " multiplos")
