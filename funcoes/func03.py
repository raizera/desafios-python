'''
função 01: validar entradas
'''

def validarEntrada(valor):
	try:
		float(valor)
		return True
	except ValueError:
		return False

valor = input('digite um número: ')

if validarEntrada(valor) == False:
	print('vc digitou um tipo errado de número!')
else:
	print('o valor digitado é válido: ', valor)
