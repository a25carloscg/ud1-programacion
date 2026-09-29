#Pedir las tres cantidades
pago_1 = float(input("Introduce lo que ha pagado el primer amigo: "))
pago_2 = float(input("Introduce lo que ha pagado el segundo amigo: "))
pago_3 = float(input("Introduce lo que ha pagado el tercer amigo: "))

#Calcular el gasto total
gasto_total = pago_1
gasto_total += pago_2
gasto_total += pago_3

#Calcular la media por persona
media = gasto_total / 3

#Calcular el balance de cada amigo
# (Resultado positivo = le deben dinero / Resultado negativo = debe dinero)
balance1 = pago_1 - media
balance2 = pago_2 - media
balance3 = pago_3 - media

#Mostrar los resultados
print("\n--- RESUMEN DE GASTOS ---")
print(f"Gasto total del viaje: {gasto_total:.2f} €")
print(f"Media que le corresponde a cada uno: {media:.2f} €")
print("\n--- BALANCES INDIVIDUALES ---")

#pago 1
if balance1 > 0:
    print(f"Al amigo 1 le deben: {balance1:.2f} €")
elif balance1 < 0:
    print(f"El amigo 1 debe: {abs(balance1):.2f} €")
else:
    print("El amigo 1 ha pagado exactamente su parte.")

# pago 2
if balance2 > 0:
    print(f"Al amigo 2 le deben: {balance2:.2f} €")
elif balance2 < 0:
    print(f"El amigo 2 debe: {abs(balance2):.2f} €")
else:
    print("El amigo 2 ha pagado exactamente su parte.")

# pago 3
if balance3 > 0:
    print(f"Al amigo 3 le deben: {balance3:.2f} €")
elif balance3 < 0:
    print(f"El amigo 3 debe: {abs(balance3):.2f} €")
else:
    print("El amigo 3 ha pagado exactamente su parte.")