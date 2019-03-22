lista = []
aux = 0

for i in range (0, 20):
    lista.append(int(input()))

for i in range (-10, 0):
    aux = lista[i]
    lista[i] = lista[(i*(-1))-1]
    lista[(i*(-1))-1] = aux

for i in range (0, 20):
    print("N[%d] = " % i + str(lista[i]))   