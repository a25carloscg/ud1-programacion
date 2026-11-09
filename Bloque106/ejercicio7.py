def calcular_descuento_irpf(sueldo_bruto: float | int, irpf: int) -> float:
    try:
        if sueldo_bruto < 0 or irpf < 0 or irpf > 100:
            raise ValueError
        return sueldo_bruto * (irpf / 100)
    except TypeError:
        return "Error: Debes introducir números."
    except ValueError:
        return "Error: Los datos introducidos no son válidos."

    #Introducir Datos:
SueldoBruto = float(input("Introducir el sueldo Bruto: "))
irpf = int(input("Introducir IRPF: "))
    #Llamada a la Función:
print(calcular_descuento_irpf(SueldoBruto, irpf))
print(calcular_descuento_irpf("1500", 15))