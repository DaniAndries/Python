año = 2

while año != 0:
    dia = int(input())
    mes = int(input())
    año = int(input())
    
    if año < 1583:
        print("Error, año inválido")
        continue
    
    A = int((14 - mes) / 12)
    B = int(año - A)
    C = int(mes + (12 * A) - 2)
    D = int(B/ 4)
    E = int(B / 100)
    F = int(B / 400)
    G = int((C * 31) / 12)
    H = int(dia + B + D - E + F + G)
    I = int(H % 7)
    
    if I == 0:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Domingo")
    elif I == 1:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Lunes")
    elif I == 2:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Martes")
    elif I == 3:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Miercoles")
    elif I == 4:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Jueves")
    elif I == 5:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Viernes")
    elif I == 6:
        print("Dia ", dia, " del mes ", mes, " del año ", año, " es Sabado")