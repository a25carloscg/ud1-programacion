a = float(input("Introduce el primer lado: "))
b = float(input("Introduce el segundo lado: "))
c = float(input("Introduce el tercer lado: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Esos lados no forman un triángulo válido")
elif a == b and b == c:
    print("Es un triángulo equilátero")
elif a == b or a == c or b == c:
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")
