numero=input()
numero=int(numero)

if numero<0:
    print("El número no es positivo")
else:
    factorial = 1
    contador = 1
    while contador <=numero:
        factorial=factorial*contador
        contador=contador+1
    print(factorial)