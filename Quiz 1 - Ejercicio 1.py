# Fabio Carrozza. C.I: 30714977.  Carnet: 20241110142

lista = [15, 13, 45, 7, 5, 123,34,12, 13,35, 19, 18, 21, 17, 60]

#Variables iniciales
respuesta = []
x = 0
y = 0
z = 0
direccion = True

# Input

# Analizar las cifras del input
for i in range(len(lista)):
    if (lista[i] % 3) == 0:
        if (lista[i] % 3) == 0 and (lista[i] % 5) == 0:
            respuesta.append("FizzBuzz")
        else:
            respuesta.append("Fizz")

    elif (lista[i] % 5) == 0:
        respuesta.append("Buzz")

    elif (lista[i] % 3) != 0 and (lista[i] % 5) != 0:
        respuesta.append("Zzzz")

    else:
        pass

print(respuesta)

for i in range(len(respuesta)):
    if direccion == True:
        if respuesta[i] == "Fizz":
            x += 1
        
        elif respuesta[i] == "Buzz":
            y += 1
        
        elif respuesta[i] == "FizzBuzz":
            z += 1

        elif respuesta[i] == "Zzzz":
            direccion = False

        else: 
            pass

    elif direccion == False:
        if respuesta[i] == "Fizz":
            x -= 1
        
        elif respuesta[i] == "Buzz":
            y -= 1
        
        elif respuesta[i] == "FizzBuzz":
            z -= 1

        elif respuesta[i] == "Zzzz":
            direccion = True

        else: 
            pass

    else:
        print("Para. Qué está pasando?")


# Respuesta final
print(f"x: {x} ---- y: {y} ---- z: {z} ---- direccion: {direccion}")