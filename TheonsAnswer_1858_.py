e = int(input())
lista = []
inp = input().split(" ")
lista.extend(inp)

for i in range (0, e):
    lista[i] = int(lista[i])

salva = min(lista)

print(lista.index(salva)+1)
