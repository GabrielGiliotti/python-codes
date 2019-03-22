p = int(input())

lista= []
soma = 0

for i in range (0, p):
    lista.append(input().split())


for i in range(0, p):
    if( lista[i][0] == '1001' ):
        lista[i][1] = int( lista[i][1] )
        soma = soma + (lista[i][1]*1.5)
    if( lista[i][0] == '1002' ):
        lista[i][1] = int( lista[i][1] )
        soma = soma + (lista[i][1]*2.5)
    if( lista[i][0] == '1003' ):
        lista[i][1] = int( lista[i][1] )
        soma = soma + (lista[i][1]*3.5)
    if( lista[i][0] == '1004' ):	
        lista[i][1] = int( lista[i][1] )
        soma = soma + (lista[i][1]*4.5)
    if( lista[i][0] == '1005' ):
        lista[i][1] = int( lista[i][1] )
        soma = soma + (lista[i][1]*5.5)


print("%.2f" % soma)