peso = float(input("Introduce tu peso (kg): "))
altura = float(input("Introduce tu altura (m): "))

imc = peso / altura ** 2

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
