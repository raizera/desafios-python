simbolo = "#"
k = 0
while k < 3:
    for i in range(1, 4):
        print(simbolo*i)
    for j in range(4, 1, -1):
        print(simbolo*j)
    k+=1