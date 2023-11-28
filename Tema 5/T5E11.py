sumaPares = 0
sumaImpares = 0
for i in range(100, 201):
    if i % 2 == 0:
        sumaPares = sumaPares + i
    else:
        sumaImpares = sumaImpares + i
print("Suma pares: ", sumaPares, "Suma impares: ", sumaImpares)
