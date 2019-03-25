# O dificil desse problema eh a leitura e selecao dos dados em python, nao o problema em si. 
lista = []
result = []
e = input().split(" ")
lista.extend(e)

A = 0
N = 0 
flag = 0
flag2 = 0
for i in range (0, len(lista)):
    lista[i] = int(lista[i])
    if(lista[i] > 0 and flag == 0):
        A = lista[i]
        lista[i] = 0
        flag = 1
    if(lista[i] > 0 and flag2 == 0):
        N = lista[i]
        lista[i] = 0
        flag = 1

soma = A    
for i in range(1, N):
    soma = soma + A + i

print(soma)  
