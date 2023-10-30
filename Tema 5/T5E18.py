numero = 2

while numero % 5 != 0:
    numero = int(input())
if numero >= 500:
    b500 = numero / 500
    numero = numero % 500
    print("500 ", int(b500))

if numero >= 200:
    b200 = numero / 200
    numero = numero % 200
    print("200 ", int(b200))

if numero >= 100:
    b100 = numero / 100
    numero = numero % 100
    print("100 ", int(b100))

if numero >= 50:
    b50 = numero / 50
    numero = numero % 50
    print("50 ", int(b50))

if numero >= 20:
    b20 = numero / 20
    numero = numero % 20
    print("20 ", int(b20))

if numero >= 10:
    b10 = numero / 10
    numero = numero % 10
    print("500 ", int(b10))

if numero >= 5:
    b5 = numero / 5
    numero = numero % 5
    print("5 ", int(b5))
