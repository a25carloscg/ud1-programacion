#Pedir kilometros recorridos, consumo del coche(Litros por cada 100KM) y precio del litro de combustible.

k = float(input("Introduce los kilómetros recorridos: "))
cons = float(input("Introduce los Litros que consume el coche en ele viaje: "))
precio = float(input("Introduce precio combustible: "))
#calcular coste del viaje.

l = cons / 100
cost = k * l * precio
#mostrar costo del viaje.

print(f"El coste total del viaje de {k} kilómetros en coche a {precio} €/L es de {cost}€")