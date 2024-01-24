import random

global v_jugador 
v_jugador = 0
global v_oponente 
v_oponente = 0

def juego(x):
    
    v_jugador = 0
    v_oponente = 0

    while (v_jugador != x) and (v_oponente != x):

        elec_jugador = 0
        elec_oponente = 0


        while elec_jugador != "piedra" and elec_jugador != "papel" and elec_jugador != "tijeras":
            elec_jugador = input("Piedra, papel o tijeras: ").lower().strip()


        elec_oponente = random.randrange(1, 4)
        

        if elec_oponente == 1:
            elec_oponente = "piedra"

        elif elec_oponente == 2:
            elec_oponente = "papel"

        else:
            elec_oponente = "tijeras"

        print (f"Tú escogiste {elec_jugador}, yo escogí {elec_oponente}")


        if elec_oponente == elec_jugador:
            print("Hubo un empate")

        elif elec_oponente == "piedra" and elec_jugador == "tijeras":
            v_oponente += 1
            print ("Te gané")

        elif elec_oponente == "piedra" and elec_jugador == "papel":
            v_jugador += 1
            print ("Me ganaste")

        elif elec_oponente == "tijeras" and elec_jugador == "piedra":
            v_jugador += 1
            print ("Me ganaste")

        elif elec_oponente == "tijeras" and elec_jugador == "papel":
            v_oponente += 1
            print ("Te gané")

        elif elec_oponente == "papel" and elec_jugador == "tijeras":
            v_jugador += 1
            print ("Me ganaste")

        else:
            v_oponente += 1
            print ("Te gané")


    if v_oponente < v_jugador:
        print("Felicidades, eres el vencedor")

    else: 
        print("Lo siento, perdiste, suerte la próxima")


print("Bienvenido, a continuación vamos a jugar Piedra, Papel o Tijeras")

y = 0

while y < 1:

    try:
        y = int(input("Al primero de cuántas partidas ganadas: "))

    except ValueError:
        print("Por favor, escribe un entero mayor a cero")
        pass

juego(y)