dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

if dia < 1 or mes < 1 or mes > 12:
    print("Fecha no válida")
else:
    if mes == 2:
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    bisiesto = True
                else:
                    bisiesto = False
            else:
                bisiesto = True
        else:
            bisiesto = False

        if bisiesto:
            dias_mes = 29
        else:
            dias_mes = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes = 30
    else:
        dias_mes = 31

    if dia <= dias_mes:
        print("Fecha válida")
    else:
        print("Fecha no válida")
