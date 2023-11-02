mayor = int(-99999999)
cantidad = 0
entradas = 0
print("Cantidad de entradas a la ventad")
cantidad = int(input())

while cantidad > 0:
    print("Hay", cantidad, "de entradas a la venta")
    entradas = int(input())
    while entradas > 10 or entradas < 0:
        print("Cantidad de entradas inválida")
        entradas = int(input())
        continue
    if entradas > mayor:
        mayor = entradas
    cantidad = cantidad - entradas
print("La mayor cantidad de entradas vendidas es", mayor)
