precio = float(input("Introduce el precio unitario: "))
cantidad = int(input("Introduce la cantidad de artículos: "))
socio = input("¿Es socio? (s/n): ")

importe = precio * cantidad

if cantidad >= 3:
    importe = importe * 0.90
    if socio == "s":
        importe = importe * 0.95
else:
    if socio == "s":
        importe = importe * 0.95

print(f"Importe total: {importe:.2f} €")
