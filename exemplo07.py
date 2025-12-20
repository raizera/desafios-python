numeros = range(10, 1, -1) #armazena umaa lista de números ao contrário

multiplicar_por_dois = map(
    lambda x: x * 2, 
    filter(
        lambda x:x % 2 == 0, numeros
        )
    )

print(list(multiplicar_por_dois))