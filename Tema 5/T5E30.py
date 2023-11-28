maximo = int(input())

for i in range(0, maximo + 1):
    for j in range(0, maximo - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print("")
