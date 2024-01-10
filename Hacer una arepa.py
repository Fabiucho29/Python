def main():

    print ("A continuación, vamos a preparar una Arepa")

    print (arepa())

    print ("Espero disfrutes la arepa")

def arepa():
    agua = float(input("Número de tazas de agua: "))
    harina = float (input("Número de tazas de harina: "))
    sal = float (input("Número de cucharaditas de sal: ")) / 48
    aceite = float(input("Número de cucharadas de aceite: ")) / 16

    bol = round(agua + harina + sal, 3)

    budare = bol + aceite

    plato = round(budare, 3)

    return f"En el bol hay {bol} tazas. Por otro lado, tanto en el budare como en el plato hay {plato} tazas."

if __name__ == "__main__":
    main()