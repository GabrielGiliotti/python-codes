lista = []
for i in range(0, 5):
    lista.append(int(input()))

par = 0

for i in range(0,5):
    if(lista[i] % 2 == 0):
        par += 1

print(par,"valores pares")