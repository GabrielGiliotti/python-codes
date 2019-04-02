def func_quad( matriz, posi, posj ):
    cont = 0
    if(matriz[posi][posj] == '1' ):       
        cont += 1
    if(matriz[posi][posj+1] == '1' ):       
        cont += 1
    if(matriz[posi+1][posj] == '1' ):       
        cont += 1
    if(matriz[posi+1][posj+1] == '1' ):       
        cont += 1
    return cont


N = int(input()) 
matriz = []
for i in range (0, N+1):
    matriz.append(input().split(" "))

cont = 0
for i in range(0, N):
    for j in range(0,N):
        cont = func_quad( matriz,i,j)
        if( cont >= 2 ):
            matriz[i][j] = 'S'
        else:
        	matriz[i][j] = 'U'

for i in range(0, N):
    for j in range(0,N):
        print(matriz[i][j], end="")
        if(j == N-1):
            print()