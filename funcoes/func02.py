def divisor(a, b):
	try:
		return float(a) / float(b)
	except ZeroDivisionError:
		return None

a = input('digite o primeiro valor: ')

b = input('digite o segundo valor: ')

resultado = divisor(a, b)

if resultado == None:
	print('você está dividindo por zero!')
else:
	print('o resultado é: ', resultado)