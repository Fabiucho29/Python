def isomorfico (x, y):
    if len(x) != len(y):
        return False
    else:
        result = []
        dic = {}
        dic[f"{x[0]}"] = y[0]
        z = ""
        for i in range(len(x)):
            if x[i] in dic.keys():
                if dic.get(x[i]) != y[i]:
                    result.append(False)
                elif dic.get(x[i]) == y[i]:
                    result.append(True)
                else:
                    print("Para. Qué está pasando?")

            else:
                dic[f"{x[i]}"] = y[i]

        print(dic)

        if False in result:
            return False
        else:
            return True
        
def main():
    s = input("Palabra: ")
    t = input("Palabra: ")
    print(isomorfico(s,t))

main()