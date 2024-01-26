check = [False, False]

direcciones = ["gmail", "hotmail", "yahoo", "estudiante"]   

sufijos = [".edu", ".com", ".org"]

while check != [True, True]:

    email = input("Ingrese su correo: ")

    # Isalpha te retorna True si todas los caracteres de la variable son letras

    if not "@" in email and not "." in email:
        if email.isalnum():
            for i in email:
                
                if i.isupper():
                    check[0] = True

                elif i.islower():
                    check[1] = True


x = 0

while x < 1 or (len(direcciones) < x):
    
    for i in range(len(direcciones)):
        print(f"{i + 1}  {direcciones[i]}")

    x = int(input("Escoja el número de la dirección que desea: "))

    if x < 1 or (len(direcciones) < x):
        print("Por favor escoja una de las opciones")

u = direcciones[x - 1]


y = 0

while y < 1 or (len(sufijos) < y):
    
    for i in range(len(sufijos)):
        print(f"{i + 1}  {sufijos[i]}")

    y = int(input("Escoja el número del sufijo que desea: "))

    if y < 1 or (len(sufijos) < y):
        print("Por favor escoja una de las opciones")

v = sufijos[y - 1]

print("Email: " + email + "@" + u + v)