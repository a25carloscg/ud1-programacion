#pedir base y altura para calcular el área.

base = float(input("Introducir base calculo área: "))
alt = float(input("Introducir altura calculo área: "))
r = float(input("Introducir radio calculo área: "))
PI = 3.1416

#calculo área triángulo.

print("área Triángulo: ", base * alt / 2)
print("perimetro_circulo: ", 2 * PI * r)
print("área_circulo: ", PI * (r ** 2))