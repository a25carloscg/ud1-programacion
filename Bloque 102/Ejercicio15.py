# Pedir km
km = float(input("Introduce la distancia en kilómetros: "))

# conversión definidos como constantes
KM_A_METROS = 1000.0
KM_A_MILLAS = 0.621371
KM_A_PIES = 3280.84

metros = km * KM_A_METROS
millas = km * KM_A_MILLAS
pies = km * KM_A_PIES

# resultados
print(f"\n--- CONVERSIÓN DE {km} KM ---")
print(f"Metros: {metros:.2f} m")
print(f"Millas: {millas:.4f} mi")
print(f"Pies: {pies:.2f} ft")