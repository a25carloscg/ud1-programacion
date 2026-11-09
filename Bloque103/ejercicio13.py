horas = float(input("Introduce las horas de estancia: "))

horas_base = horas if horas <= 4 else 4
horas_extra = horas - 4 if horas > 4 else 0

if horas <= 1:
    importe = 0
else:
    importe = 1.5 * horas_base + 1 * horas_extra

print(f"Importe a pagar: {importe:.2f} €")
