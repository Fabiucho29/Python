import random

Ps_jugador = 100
Ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

while Ps_jugador > 0 and Ps_oponente > 0: 

    print("La vida del jugador es", Ps_jugador)

    print("La defensa del jugador es", defensa_jugador)

    print("La vida del oponente es", Ps_oponente)

    print ("La defensa del oponente es", defensa_oponente)

    ataque_jugador = input("Ataque: ")
    ataque_jugador = ataque_jugador.lower()

    if ataque_jugador == "malicioso":
        defensa_oponente -= 10
        if defensa_oponente <= 0:
            defensa_oponente = 1
    
    elif ataque_jugador == "placaje":
        Ps_oponente -= (35 / (defensa_oponente/100))

    elif ataque_jugador == "ascuas":
        Ps_oponente -= 20
    
    else:
        print ("Qué estas haciendo? Tus ataques son malicioso, placaje y ascuas")
        continue


    # Turno del Oponente
    # El turno del oponente se define como un Random

    ataque_oponente = random.randrange (1, 3+1)

    if ataque_oponente == 1: #latigo
        print ("Te ataco con látigo")
        defensa_jugador -= 10
        if defensa_jugador <= 0:
            defensa_jugador = 1

    elif ataque_oponente == 2: #placaje
        print("Te ataco con placaje")
        Ps_jugador -= (35 / (defensa_jugador/100))

    else: #pistola de agua
        print("Te ataco con pistola de agua")
        Ps_jugador -= 40

if Ps_jugador <= 0:
    print ("Has perdido, suerte la próxima")

else: 
    print ("Felicidades, eres un gran maestro Pokemon")