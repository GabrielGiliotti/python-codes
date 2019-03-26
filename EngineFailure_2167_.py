lista = []
N = int(input())

inp = input().split(" ")
lista.extend(inp)

for i in range(0, N):
	lista[i] = int(lista[i])

ind = 0
for i in range(1, N):
    if(lista[i] < lista[i-1]):
        ind = i+1
        break    

print(ind)