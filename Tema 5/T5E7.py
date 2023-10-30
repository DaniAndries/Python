negativos=0
positivos=0
for i in range (0,10):
    numero=int(input())
    if numero<0:
        negativos=negativos+1
    else:
        positivos=positivos+1
print("Positivos: ",positivos," negativos: ",negativos)