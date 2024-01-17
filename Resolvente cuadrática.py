import math

def resolvente(a, b, c):
    discriminante = (b**2 - (4 * a * c))

    if discriminante < 0: 
        return "Esta función no tiene soluciones reales"
    
    elif discriminante == 0:
        solucion_0 = round((-b / (2 * a)), 4)

        return f"{solucion_0} es la única solución de esta función"
    
    else: 

        discriminante = math.sqrt(discriminante)

        solucion_1 = round(((-b + discriminante) / (2 * a)), 4)
        solucion_2 = round(((-b - discriminante) / (2 * a)), 4)

        return f"{solucion_1} y {solucion_2} son los 2 puntos de corte en x (soluciones)"

print ("A continuación, escriba los valores que tiene c/u de los coeficientes en una función cuadrática")

print ("Recordando: a (coeficiente cuadrático), b (coeficiente lineal), c (término independiente)")

while True:
    try:
        a = int(input("a (distinto de 0): "))

        if a == 0:
            raise ValueError
        
    except ValueError:
        print ("Por favor escriba un entero")

    else: 
        break

while True:
    try:
        b = int(input("b: "))
    
    except ValueError:
        print ("Por favor escriba un entero")

    else: 
        break

while True:
    try:
        c = int(input("c: "))
    
    except ValueError:
        print ("Por favor escriba un entero")

    else: 
        break

print(resolvente(a, b, c))