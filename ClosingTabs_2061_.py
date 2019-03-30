N, M = input().split(" ")
N = int(N)
M = int(M)
lista = []
for i in range(0,M):
    lista.append(input())

for i in range(0,M):
    if(lista[i] == 'fechou'):
        N = N + 1

    if(lista[i] == 'clicou'):
        N = N - 1

print(N)
