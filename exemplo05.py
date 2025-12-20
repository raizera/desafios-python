'''
Docstring for exemplo05

tarefa 02 - separação de dados
'''
texto = "nome, idade, cidade"

texto_espacos = texto.replace(' ', '')

texto_lista = texto_espacos.split(',')

for i in texto_lista:
    print(i)