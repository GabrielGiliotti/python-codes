N1 = int(input())
N2 = int(input())
soma = 0
if( N1 < N2 ):
	lista = list(range(N1,N2,1))
else:
    lista = list(range(N2,N1,1))

for i in range(1, len(lista)):
    if(lista[i] < 0):
        aux = lista[i]*(-1)
        if( aux % 2 != 0 ):
            soma = soma + lista[i]
    else:
        if( lista[i] % 2 != 0 ):
            soma = soma + lista[i]

print(soma)