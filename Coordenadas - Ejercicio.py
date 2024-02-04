def camino(z):
    movimientos = [(0,0)]
    x = 0
    y = 0
    direccion = False
    for i in z:
        if i == "N":
            y += 1
        elif i == "S":
            y -= 1
        elif i == "E":
            x += 1
        elif i == "W":
            x -= 1
        else:
            print("Para. Qué está pasando?")

        if (x,y) in movimientos:
            direccion = True

        movimientos.append((x,y))

    return f"""Esta fue la lista de movimientos: {movimientos}
--- {direccion}"""

def main():  
    path = input("Dime el camino (NSEW): ")
    path = path.upper()
    print(camino(path))

main()