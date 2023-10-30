inferior = 1
superior = 100
numero = 0
prepuesta = 0
while numero != 3:
    propuesta = (inferior + superior) / 2
    print(int(propuesta))
    numero = int(input())
    if numero == 1:
        inferior = propuesta + 1
    elif numero == 2:
        superior = propuesta + 1
print(numero)
