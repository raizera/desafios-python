'''
Docstring for exemplo09

somar vetores com map
'''

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

soma = list(map(lambda x, y, z: x + y + z, a, b, c))

print(soma)