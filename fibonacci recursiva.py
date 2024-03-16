def fibonacci(serie):
    
    if len(serie) == 0:
        serie.append(1)

    if len(serie) == 1:
        serie.append(1)

    if len(serie) > 1:
        if len(serie) < 200:
            serie.append(serie[len(serie) - 1] + serie[len(serie) - 2])
            fibonacci(serie)

        if len(serie) >= 200:
            return serie
        
serie = []
result = fibonacci(serie)
print(len(result))