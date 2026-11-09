jugada1 = input("Jugador 1 (piedra, papel o tijera): ")
jugada2 = input("Jugador 2 (piedra, papel o tijera): ")

if jugada1 == jugada2:
    print("Empate")
elif jugada1 == "piedra":
    if jugada2 == "tijera":
        print("Gana el jugador 1")
    else:
        print("Gana el jugador 2")
elif jugada1 == "papel":
    if jugada2 == "piedra":
        print("Gana el jugador 1")
    else:
        print("Gana el jugador 2")
else:
    if jugada2 == "papel":
        print("Gana el jugador 1")
    else:
        print("Gana el jugador 2")
