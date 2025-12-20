'''
Docstring for exemplo06

usanod função filter para filtrar
'''

idades = [12, 18, 25, 14, 30]

maiores = list(filter(lambda x:x >= 18, idades)) #filter aqui

maiores_outro_met = [x for x in idades if x >= 18] #sem filter aqui

print(maiores)
print(maiores_outro_met)