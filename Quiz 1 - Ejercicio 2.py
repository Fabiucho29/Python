# Fabio Carrozza. C.I: 30714977.  Carnet: 20241110142

# Matriz input 

           # Tendencia,   #Vistas   #Likes
matriz = [["Mano tengo Fe", 44833, 788],
          ["coquette", 56048, 428], 
          ["donalt trump", 2597, 100], 
          ["cambien la semana de retiro", 89705, 1198], 
          ["pelusa", 14708, 222]]


# Lista auxiliar
porcentaje = []

for i in range(len(matriz)):
    porcentaje.append(round(((((matriz[i])[2]) / ((matriz[i])[1])) * 100), 2))

print(porcentaje)

# Resultado
x = max(porcentaje)

y = porcentaje.index(x)

# Final del programa
print(f"La tendencia más buscada fue {matriz[y][0]}")