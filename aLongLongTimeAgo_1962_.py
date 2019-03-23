N = int(input())
lista = []

for i in range (0, N):
    lista.append(int(input()))

for i in range (0, N):
    lista[i] = lista[i]-2015
    if( lista[i] < 0):
        lista[i] = lista[i] * (-1)
        print(lista[i], "D.C.")
    else:
        lista[i] = lista[i] + 1
        print(lista[i], "A.C.")
