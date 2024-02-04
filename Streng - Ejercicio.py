def streng(x, k):
    respuesta = []
    for i in range(len(x)):
        if x[i] not in respuesta:
            respuesta.append(x[i])

        elif x[i] in respuesta:
            respuesta.remove(x[i])

        else:
            print("Para. Qué está pasando?")

    if k > len(respuesta):
        return ""
    
    else:
        return respuesta[k - 1]
    

def main():
    string = ""
    while string == "" or string == " " or string == "  ":
        string = input("Coloque una lista de caracteres: ")

    num = 0
    while 1 > num:
        try:
            num = int(input("Entero positivo: "))
        except ValueError:
            print("Por favor coloque un entero positivo")

    print(streng(string, num))

main()