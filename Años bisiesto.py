def main():
    while True:
        try:
            numero = int(input("Número entre 1900 y 2199: "))
            if numero < 1900 or numero > 2199:
                raise ValueError
        except ValueError:
            print ("Coloque un número válido")
        else: 
            break
    
    print(bisiesto(numero))

    print(bisiesto_total(numero))

def bisiesto(n):
    if n%4 ==0:
        if n%100 == 0 and n%400 != 0:
            return f"{n} no es un año bisiesto"
        else: 
            return f"{n} es un año bisiesto"
        
    else:
        return f"{n} no es un año bisiesto"

def bisiesto_total(n):
    diferencia = n - 1900
    if diferencia == 0:
        return f"Hay 0 años bisiestos entre {n} y 1900 porque son el mismo número"
    else:
        if diferencia < 200:
            final = diferencia // 4
            return f"Hay {final} años bisiestos entre 1900 y {n}"
        else:
            final = (diferencia // 4) - 1
            return f"Hay {final} años bisiestos entre 1900 y {n}"
        

if __name__ == "__main__":
    main()