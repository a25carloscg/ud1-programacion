# PEDIR GASTOS
amigo1 = float(input("Introduce lo que ha pagado el primer amigo: "))
amigo2 = float(input("Introduce lo que ha pagado el segundo amigo: "))
amigo3 = float(input("Introduce lo que ha pagado el tercer amigo: "))

# CALCULO
gasto_total = 0
gasto_total += amigo1
gasto_total += amigo2
gasto_total += amigo3

media = gasto_total / 3

balance_amigo1 = amigo1 - media
balance_amigo2 = amigo2 - media
balance_amigo3 = amigo3 - media

# RESULTADO
print(f"\nGasto total del viaje: {gasto_total:.2f}€")
print(f"A cada uno le corresponde pagar (media): {media:.2f}€\n")
print(f"Balance del primer amigo: {balance_amigo1:.2f}€")
print(f"Balance del segundo amigo: {balance_amigo2:.2f}€")
print(f"Balance del tercer amigo: {balance_amigo3:.2f}€")