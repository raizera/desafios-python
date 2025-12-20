palavra = input("Digite uma palavra: ")

palavra_sem_espacos = palavra.strip()

try:
    int(palavra_sem_espacos)
    possui_numeros = True
    print("A palavra contém números. Por favor, digite apenas letras.")
except ValueError:
    possui_numeros = False

tamanho = len(palavra_sem_espacos)

if tamanho % 2 == 0:
    print("A palavra {palavra_sem_espacos} tem um número par de letras.".format(palavra_sem_espacos=palavra_sem_espacos))
else:
    print("A palavra {palavra_sem_espacos} tem um número ímpar de letras.".format(palavra_sem_espacos=palavra_sem_espacos))