import math

a = float(input("Introduce el primer lado: "))
b = float(input("Introduce el segundo lado: "))
c = float(input("Introduce el tercer lado: "))

if a >= b:
    if a >= c:
        mayor = a
        otro1 = b
        otro2 = c
    else:
        mayor = c
        otro1 = a
        otro2 = b
else:
    if b >= c:
        mayor = b
        otro1 = a
        otro2 = c
    else:
        mayor = c
        otro1 = a
        otro2 = b

if math.isclose(mayor ** 2, otro1 ** 2 + otro2 ** 2):
    print("Es un triángulo rectángulo")
else:
    print("No es un triángulo rectángulo")
