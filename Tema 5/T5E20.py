numero1 = 0
numero2 = 1
cantidad = int(input())
contador = int(cantidad / 2)
for i in range(0, contador):
    print(numero1)
    numero1 = numero1 + numero2
    print(numero2)
    numero2 = numero1 + numero2
if cantidad % 2 != 0:
    print(numero1)
