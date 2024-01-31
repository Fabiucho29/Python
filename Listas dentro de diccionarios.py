Ps_oponente = 100
Ps_defensa = 1

d = {"nombre": ["malicioso", "placaje", "ascuas"],
"daño": [0, 15, 20],
"efecto": [0.1, 0, 0]}

z = 0

while Ps_oponente > 0:

    x = 0

    while x not in d["nombre"]:
        x = input ("Ataque: ")

    i = d["nombre"].index(x)

    print(i)

    Ps_defensa -= d["efecto"][i]

    Ps_oponente -= (d["daño"][i] / Ps_defensa)

    z += 1

    print (f"En el turno {z} la vida del oponente es {Ps_oponente} y la defensa {Ps_defensa}")


print("Ha terminado el juego")