N = int(input())
lista = []
inp = input().split(" ")
lista.extend(inp)
div2 = 0
div3 = 0
div4 = 0
div5 = 0

for i in range (0,N):
    lista[i] = int(lista[i])

for i in range(0,N):
    if(lista[i] % 2 == 0 ):
        div2 += 1
    if(lista[i] % 3 == 0 ):
        div3 += 1
    if(lista[i] % 4 == 0 ):
        div4 += 1
    if(lista[i] % 5 == 0 ):
        div5 += 1

print(str(div2) + " Multiplo(s) de 2")
print(str(div3) + " Multiplo(s) de 3")
print(str(div4) + " Multiplo(s) de 4")
print(str(div5) + " Multiplo(s) de 5")