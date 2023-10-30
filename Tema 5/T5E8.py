numero=1
positivos=0
negativos=0
while numero != 0:
    numero=int(input())
    if numero<0:
        negativos=negativos+1
    else:
        positivos=negativos+1
print("Positivos: ",positivos," Negativos: ",negativos)