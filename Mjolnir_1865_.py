C = int(input())
lista = []
for i in range(0 , C):
    lista.append(input().split(" "))

for i in range(0, C): 
    if( lista[i][0] == "Thor"):
        print("Y")
    else:
        print("N")