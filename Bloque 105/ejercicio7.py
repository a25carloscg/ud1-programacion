def convertir_temperatura(grados, a_fahrenheit=True):
    if a_fahrenheit:
        return grados * 9/5 + 32
    else:
        return (grados - 32) * 5/9

# Sin el segundo argumento (usa valor por defecto: Celsius a Fahrenheit)
print(convertir_temperatura(25))

# Con el argumento en posición (Fahrenheit a Celsius)
print(convertir_temperatura(77, False))

# Con el argumento como argumento con nombre (Fahrenheit a Celsius)
print(convertir_temperatura(100, a_fahrenheit=False))
