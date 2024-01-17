print ("Ahora te vas a adentrar a un nuevo mundo! ")

w = "Bienvenid"

x = input("Eres chico o chica?" )

if x == "chico":
    w += "o"

else:
    w += "a"

print (w, "al mundo de los Pokemon")

y = int(input("Que edad tienes? "))

if y <= 10:
    if x == "chico":
        print ("No tienes edad para ser entrenador")
        quit()
    else: 
        print ("No tienes edad para ser entrenadora")
        quit()

else: 
    print ("Vamos!")

reg = input("Necesitarás un compañero de viaje. En qué región te encuentras?")

if reg == "Kanto" and x == "chico":
    print ("Tu compañera de viaje es Misty")

else: 
    print ("Tu compañero de viaje es Brook!")

tipo = input("Que tipo de pokemon queres para empezar? ")

if tipo == "agua":
    print ("Tu starter es Oshawott")

elif tipo == "fuego":
    print ("Tu starter es Cyndaqui")

else: 
    print ("Tu starter es Rowlet")