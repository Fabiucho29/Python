def heights(x):
    z = sorted(x)
    y = 0
    for i in range(len(x)):
        if x[i] != z[i]:
            y += 1

    print(z)
    return y

def main():
    alturas = [1,1,4,2,1,3]
    print(heights(alturas))

main()