#python tem lista com indice negativo
lista = []
V = int(input())
lista.append(V)

for i in range (0,9):
    lista.append(lista[i]*2)

for i in range (0,10):
    print("N[%d] = " % i + str(lista[i]))  