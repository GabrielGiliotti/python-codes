lista = []
for i in range(0,10):
    lista.append(int(input()))

for i in range(0,10):
    if(lista[i] <= 0):
        lista[i] = 1
    print("X[%d] = " % i + str(lista[i]))
