def suma_max(x):
    respuesta = []
    y = min(x[0], x[1])
    z = min(x[2], x[3])

    respuesta.append(y + z)

    y = min(x[0], x[2])
    z = min(x[1], x[3])

    respuesta.append(y + z)

    y = min(x[0], x[3])
    z = min(x[1], x[2])

    respuesta.append(y + z)

    return f"""Esta fue la lista: {respuesta}
y este su máximo: {max(respuesta)}"""

def main():
    nums = [1,4,3,2]
    print(suma_max(nums))

main()