N = int(input())
lista = []
soma = 0
for i in range(0, N):
    lista.append(int(input()))

for i in range(0, N):
    if(lista[i] == 2 or lista[i] == 3):
        soma += 1

print(soma)
