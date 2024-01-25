def palindromo(x):

    lista = []

    for i in range(len(x)):
        lista.append(x[i])


    lista_n = []


    for i in range ((len(lista) - 1), -1, -1):
        lista_n.append(lista[i])


    if lista == lista_n:
        return f"{x} es un palíndromo"
    
    else:
        return f"{x} no es un palíndromo"
    

print("Un palíndromo es una palabra o un número que se lee igual al derecho y al revés")

y = None

while y == None:
    y = input("Escribe una palabra o un número: ").strip().lower()

    if y == "" or y == " " or y == "  ":
        y = None

print(f"Vamos a comprobar si {y} es un palíndromo")

print(palindromo(y))