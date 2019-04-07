X = int(input())
while True:
    try:
        Z = int(input())
        if(Z > X):
            break
    except EOFError:
        break
    
cont = 1
soma = 0
for i in range(X,Z):
    soma = soma + i
    if( soma < Z ):
        cont += 1
print(cont)