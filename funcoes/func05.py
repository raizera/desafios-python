def calcular_media(lista):
	if len(lista) == 0:
		return None
	else:
		media = sum(lista) / len(lista)
	return media

lista = input("Digite uma lista de números separados por vírgula: ")
numeros = [float(num) for num in lista.split(",")] #[expressão for variável in iterável]: “Crie uma lista contendo float(num) para cada num em lista.split(",")"
print(f"A média é {calcular_media(numeros)}")