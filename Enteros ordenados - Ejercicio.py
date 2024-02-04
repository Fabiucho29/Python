def enteros(x, k):
    if k in x:
        x = sorted(x)
        print(x)
        return f"{k} está en la posición {(x.index(k) + 1)} de la lista"
    
    else:
        x.append(k)
        x = sorted(x)
        print(x)
        return f"{k} estaría en la posición {(x.index(k) + 1)} de la lista"
           
def main():
    nums = []
    x = 0
    while x < 1:
        try:
            x = int(input("Cuános números quiere en la lista: "))
        except ValueError:
            print("Coloque un entero positivo")
        else:
            pass

    for i in range(x):
        y = int(input("Agrega un entero: "))
        nums.append(y)
    

    target = 0
    while True:
        try:
            target = int(input("Dime un número para buscarlo: "))
        except ValueError:
            print("Coloca un entero")
        else:
            break

    print(enteros(nums, target))

main()