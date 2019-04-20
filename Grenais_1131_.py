Inter = 0
Gremio = 0
Empate = 0
cont = 0
while True:
    I,G = input().split(" ")
    I = int(I)
    G = int(G)
    if( I > G ):
        Inter += 1
    if( I < G ):
        Gremio += 1
    if( I == G ):
        Empate += 1
    N = int(input())
    if( N == 1 ):
        cont += 1
    if( N == 2 ):
        break

for i in range(cont+1):
    print("Novo grenal (1-sim 2-nao)")
print(cont+1, "grenais")
print("Inter:" + str(Inter))
print("Gremio:"+ str(Gremio))
print("Empates:"+str(Empate))
if( Inter > Gremio ):
    print("Inter venceu mais")
elif( Inter < Gremio ):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
