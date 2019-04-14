N = int(input())
lista = []
for i in range (N):
    lista.append(int(input()))

cont = 0
for i in range(N):
    for j in range(1, lista[i]+1):
        if(lista[i] % j == 0):
            cont += 1
    if(cont > 2):
        print(str(lista[i]) + " nao eh primo", end="\n")
    else:
        print(str(lista[i]) + " eh primo", end="\n")
    cont = 0
