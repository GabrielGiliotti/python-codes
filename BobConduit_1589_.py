T = int(input())
lista = []
rf = 0

for i in range(0, T):
    rf = 0
    r1,r2 = input().split(" ")
    r1 = int(r1)
    r2 = int(r2)
    rf = ((2*3*r1) + (2*3*r2))/6
    lista.append(rf)

for i in range(0, len(lista)):
    print(int(lista[i]))


