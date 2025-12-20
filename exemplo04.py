'''
Docstring for exemplo04

tarefa 01 - strings
'''

texto = input("digite seu texto com espaços: ")
print(texto.split())

texto_modificado = texto.replace(" ", "")

print(f'seu texto sem espaços é: {texto_modificado}')

print(f'seu texto em caps lock é: {texto_modificado.upper()}')