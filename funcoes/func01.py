def multiplicar(a, b):
	try:
		return float(a) * float(b) 
	except ValueError:
		return None

a = input('digite o primeiro número: ')
b = input('digite o segundo número: ')

resultado = multiplicar(a, b)

if resultado == None:
	print('vc digitou um caractere inválido!')
else:
	print('o resultado é: ', resultado)