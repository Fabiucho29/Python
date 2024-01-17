def factorial(n):
    result = 1

    for i in range (1, (n + 1)):
        result = result * i
        
    return f"El factorial de {n} es {result}"

while True:

    try:
        number = int(input("Escriba un número entero positivo: "))

        if number <= 0:
            raise ValueError
    
    except ValueError:
        print("Escriba un entero mayor que 0")

    else: 
        break

print(factorial(number))