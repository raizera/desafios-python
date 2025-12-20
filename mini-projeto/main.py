'''
Docstring for mini-projeto.main

usando try/excpt

'''

valor1 = input("Digite o primeiro número: ")
valor2 = input("Digite o segundo número: ")

try:
    numero1 = float(valor1)
    numero2 = float(valor2)
except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos")
else:
    try:
        resultado = numero1 / numero2
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print("O resultado da divisão é:", resultado)