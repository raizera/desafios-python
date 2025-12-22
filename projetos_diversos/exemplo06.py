'''
Docstring for exemplo06

usanod função filter para filtrar
'''

idades = [12, 18, 25, 14, 30]

maiores = list(filter(lambda x:x >= 18, idades)) #com filter

maiores_outro_metod = [x for x in idades if x >= 18] #sem filter

print(maiores)
print(maiores_outro_metod)