numero1 = 1
numero2 = 0
contador = 0
while numero1 != 0:
    numero1 = int(input())
    contador = contador + 1
    if numero1 < numero2 & numero1 != 0:
        print("error, el número es menor")
    elif numero1 > numero2:
        numero2 = numero1
    elif numero1 == 0:
        print("Total de numeros introducidos: ", (contador - 1))
