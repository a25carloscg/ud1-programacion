def calcular_precio_final(precio: float, cantidad: int, descuento: float = 0) -> float:
    total_sin_descuento = precio * cantidad
    total_con_descuento = total_sin_descuento * (1 - descuento / 100)
    return total_con_descuento


# Resultado
resultado_1 = calcular_precio_final(10.5, 4)
print(f"Compra 1 (10.5€ x 4, sin descuento): {resultado_1}€")
resultado_2 = calcular_precio_final(50.0, 2, 10)
print(f"Compra 2 (50.0€ x 2, 10% descuento): {resultado_2}€")
resultado_3 = calcular_precio_final(precio=100.0, cantidad=1, descuento=25)
print(f"Compra 3 (100.0€ x 1, 25% descuento): {resultado_3}€")
