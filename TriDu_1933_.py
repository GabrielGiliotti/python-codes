lista = []
inp = input().split(" ")
lista.extend(inp)

A = int(lista[0])
B = int(lista[1])

if( A == B ):
    print(A) #Se as cartas que entram sao iguais, uma tripla ganha de uma dupla, entao potencializamos com uma igual	
elif( A > B ):
    print(A) #Se as cartas tem valores diferentes, pegamos a maior para fazer um par com o maior possivel, potencializando a dupla
else:
    print(B)    