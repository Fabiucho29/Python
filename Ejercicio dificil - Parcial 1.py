def sumas(x):
    res_1 = []
    res_2 = []
    result = []
    res_1.append(0)
    b = len(x)
    for i in range (0, len(x) - 1):
        if i == 0:
            y = x[0]
        else:
            y += x[i]
        res_1.append(y)

    y = 0

    for i in range (len(x) - 1, 0, -1):
        if i == b:
            y = x[b]
        else:
            y += x[i]
        res_2.append(y)

    res_2.append(0)

    if len(res_1) == len(res_2):
        for i in range (len(x)):
            result.append(abs(res_1[i] - res_2[i]))

    print(res_1)
    print(res_2)
    return result


def main():
    a = [10,5,1,12]
    print(sumas(a))

main()