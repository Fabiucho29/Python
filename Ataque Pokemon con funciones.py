import random

def placaje(x, y):
    x -= (35 / (y / 100))
    return x

def malicioso(x):
    x -= 10
    return x

def ascuas(x):
    x -= 20
    return x

def pistola_de_agua(x):
    x -= 40
    return x

def latigo(x, y):
    x -= 10
    y -= 10
    return x, y

v = 0

Ps_jugador = 100
Ps_oponente = 100
defensa_oponente = 100
defensa_jugador = 100

historial_ataques = []

estadisticas = {}

ataques_live = {}

while Ps_jugador > 0 and Ps_oponente > 0: 

    print("La vida del jugador es", round(Ps_jugador, 2))

    print("La defensa del jugador es", defensa_jugador)

    print("La vida del oponente es", round(Ps_oponente, 2))

    print ("La defensa del oponente es", defensa_oponente)

    if v != 0:
        ataques_live["Ataque jugador"] = f"Se restaron {round(100 - Ps_oponente, 2)} puntos de vida y {100 - defensa_oponente} de defensa al oponente"
        ataques_live["Ataque oponente"] = f"Se le restaron {round(100 - Ps_jugador, 2)} puntos de vida y {100 - defensa_jugador} de defensa"

        print(ataques_live)

    v += 1

    x = Ps_jugador
    y = defensa_jugador
    a = Ps_oponente
    z = defensa_oponente

    ataque_jugador = input("Ataque: ")
    ataque_jugador = ataque_jugador.lower()

    if ataque_jugador == "malicioso":
        defensa_oponente = malicioso(defensa_oponente)
        if defensa_oponente <= 0:
            defensa_oponente = 1
    
    elif ataque_jugador == "placaje":
        Ps_oponente = placaje(Ps_oponente, defensa_oponente)

    elif ataque_jugador == "ascuas":
        Ps_oponente = ascuas(Ps_oponente)
    
    else:
        print ("Qué estas haciendo? Tus ataques son malicioso, placaje y ascuas")
        continue


    historial_ataques.append(ataque_jugador)

    # Turno del Oponente
    # El turno del oponente se define como un Random

    ataque_oponente = random.randrange (1, 3+1)

    if ataque_oponente == 1: #latigo
        print ("Te ataco con látigo")
        if defensa_jugador <= 0:
            defensa_jugador = 1
        Ps_jugador, defensa_jugador = latigo(Ps_jugador, defensa_jugador)
        
    elif ataque_oponente == 2: #placaje
        print("Te ataco con placaje")
        if defensa_jugador <= 0:
            defensa_jugador = 1
        Ps_jugador = placaje(Ps_jugador, defensa_jugador)

    else: #pistola de agua
        print("Te ataco con pistola de agua")
        Ps_jugador = pistola_de_agua(Ps_jugador)

    estadisticas[f"Turno {v} (Salud, Defensa)"] = [f"Jugador {round(x),round(y)}, Oponente {round(a),round(z)}"]



if Ps_jugador <= 0:
    if Ps_oponente <= 0:
        print ("Hubo un empate. Se decidirá en la revancha")

    else:
        print ("Has perdido, suerte la próxima")

else: 
    print ("Felicidades, eres un gran maestro Pokemon")

print("Por último, este fue tu historial de ataques durante la partida:")

print(historial_ataques)

print("Y esta sus estadísticas de vida y de defensa y las de su oponente respectivamente en cada turno")

print(estadisticas)