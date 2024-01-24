codigos_postales = """...._ __... ..... ..___*.____ ___.. ___.. _____*_.... ..___ ...__ _....*..... __... .____ .____*___.. ...._ ____. ____."""

codigos_postales = codigos_postales.replace("*", " ")

cant_morse = codigos_postales.count(" ") + 1

n_separados = []

for i in range (1):
    n_separados.append(codigos_postales.split(" "))

n_traducidos = []

result = []

for i in range (cant_morse):

    if (n_separados[0])[i] == ".____":
        n_traducidos.append("1")

    elif (n_separados[0])[i] == "..___":
        n_traducidos.append("2")

    elif (n_separados[0])[i] == "...__":
        n_traducidos.append("3")

    elif (n_separados[0])[i] == "...._":
        n_traducidos.append("4")

    elif (n_separados[0])[i] == ".....":
        n_traducidos.append("5")

    elif (n_separados[0])[i] == "_....":
        n_traducidos.append("6")

    elif (n_separados[0])[i] == "__...":
        n_traducidos.append("7")

    elif (n_separados[0])[i] == "___..":
        n_traducidos.append("8")

    elif (n_separados[0])[i] == "____.":
        n_traducidos.append("9")

    else:
        n_traducidos.append("0")


cant_numeros = len(n_traducidos)


for i in range (0, cant_numeros, int(cant_numeros / 5)):
    result.append(str(n_traducidos[i]) + str(n_traducidos[i + 1]) + str(n_traducidos[i + 2]) + str(n_traducidos [i + 3]))


print ("Ya está el mensaje decodificado")

print (result)