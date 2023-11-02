for i in range(2, 10000):
    sumatorio = int(1)
    for j in range (2, i-1):
        if i % j == 0:
            sumatorio += j
    if i == sumatorio:
        print(i, end=" ")