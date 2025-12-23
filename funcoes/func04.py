def calcular_media(lista):
    if lista == []:
        return None
    return sum(lista) / len(lista)

lista = input("Digite uma lista de números separados por vírgula: ")

numeros = [float(num) for num in lista.split(",")]

media = calcular_media(numeros)

print(f"A média é {media}")