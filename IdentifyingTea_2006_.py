#Nao realizo restricao sobre os numeros serem entre 1 e 5 !
T = int(input())
lista = []
lista.extend(input().split(" "))
soma = 0

for i in range(0, 5):
    if( T == int(lista[i]) ):
        soma += 1

print(soma)
