import random
#devuelve un número aleatorio entre 1 y 6.
def tirar_dado():
    return random.randint(1, 6)
#llama dos veces a la anterior y devuelve la suma.
def tirar_dos_dados():
    return tirar_dado() + tirar_dado()
#Define el programa principal
def jugar_ronda():
    puntos_jugador = tirar_dos_dados()
    puntos_banca = tirar_dos_dados()
    
    print(f"Tu puntuación: {puntos_jugador}")
    print(f"Puntuación de la banca: {puntos_banca}")
    
    if puntos_jugador > puntos_banca:
        print("¡Ganas tú!")
    elif puntos_banca > puntos_jugador:
        print("Gana la banca")
    else:
        print("Empate")

jugar_ronda()
