def metro_encoding(x):
    respuesta = []
    matriz_1 = []
    matriz_2 = []

    for _ in range(x[0]):
        matriz_1.append(x[1])

    for _ in range(x[2]):
        matriz_2.append(x[3])

    respuesta = matriz_1 + matriz_2

    return respuesta

def main():
    nums = [1,2,3,4]
    print(metro_encoding(nums))

main()