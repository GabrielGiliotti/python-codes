lista = []
N = int(input())
for i in range(N):
    lista.append(int(input()))
for i in range(N):
    if(lista[i] == 0):
        print("NULL")
    if(lista[i] < 0 and lista[i] % 2 == 0):
        print("EVEN NEGATIVE")
    if(lista[i] > 0 and lista[i] % 2 == 0):
        print("EVEN POSITIVE")
    if(lista[i] < 0 and lista[i] % 2 != 0): 
        print("ODD NEGATIVE")
    if(lista[i] > 0 and lista[i] % 2 != 0): 
        print("ODD POSITIVE")
