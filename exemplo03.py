'''
Docstring for exemplo03
estudando tratamento de erros
'''

try:
    x = int(input("Número: "))
    resultado = 10 / x
    print(resultado)
except ValueError:
    print("Digite um número")
except ZeroDivisionError:
    print("Não pode dividir por zero")
