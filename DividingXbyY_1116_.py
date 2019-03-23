#from __future__ import print_function

N = int(input())

listaX = []
listaY = []

for i in range (0, N):
    X,Y = input().split(" ")
    X = int(X)
    Y = int(Y)
    listaX.append(X)
    listaY.append(Y)
     
for i in range (0, N):
    if(listaY[i] == 0):
        print("divisao impossivel")
        continue
    else:
        print(listaX[i]/listaY[i])

