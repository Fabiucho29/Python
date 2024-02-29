from DatosQuiz import db
from game import Game
from team import Team
from person import Player, Client

jugadores_todo = db["Jugadores"]
compradores_todo = db["Compradores"]
partidos_todo = db["Partidos"]
equipos_todo = db["Equipos"]

jugadores = []
compradores = []
partidos = []
equipos = []


def downloadData(x, f):
    for i in range(len(x)):
        y = x[i]
        jugadores.append(Player(y[0], y[1], y[2], y[3]))

    for i in f:
        partidos.append(Game(i[0], i[1], i[2], i[3]))

    return jugadores, partidos

def asignar(x, a):
    for j in range(len(x)):
        for i in partidos:
            if i.id == x[j]["Partido"]:
                break
        compradores.append(Client(x[j]["Nombre"], i, x[j]["CantidadEntradas"], x[j]["Asistencia"]))

    for i in a:
        team_players = []
        for j in jugadores:
            if j.player_id in i["Jugadores"]:
                team_players.append(j)

        equipos.append(Team(i["Nombre"], team_players, i["ID"]))

    return compradores, equipos
    

def main():
    downloadData(jugadores_todo, partidos_todo)    
    asignar(compradores_todo, equipos_todo)
    while True: 
        x = int(input("""1 -- Ver equipos con sus jugadores
2 -- Ver Itinerario
3 -- Confirmar Asistencia
4 -- Comprar Boleto
5 -- Ver Estadísticas
0 -- Terminar el Programa
--"""))
        
        if x == 1:
            print("Estos son los equipos")
            for i in equipos:
                print("""
                      
                      Equipo de la Liga""")
                print(i.read())
                print("Sus jugadores son: ")
                for j in i.players:
                    print(j.read())

        if x == 0:
            quit()
        
        if x == 2:
            for i in partidos:
                print("""
                      
                      Partido de la Liga""")
                print(i.read())

        if x == 3:
            for i in range(len(compradores)):
                print(f"{i + 1} -- {compradores[i].name}")
            y = int(input("Confirme su asistencia: "))

            compradores[y - 1].assit = True

        if x == 4:
            for i in range(len(partidos)):
                print(f"{i + 1} -- {partidos[i].read()}")

            y = int(input("A cuál partido desea asistir: "))
            z = int(input("Cuantos boletos quiere: "))
            name = input("Nombre: ")

            compradores.append(Client(name, partidos[y - 1], z, True)) 


main()