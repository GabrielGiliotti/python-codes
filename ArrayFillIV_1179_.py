lista = []
for i in range (0,15):
    lista.append(int(input()))

par = []
impar = []

for i in range(0,15):
    if(lista[i] % 2 == 0):
        par.append(lista[i])
    else:
        impar.append(lista[i])
    if( len(par) == 5 ):
        for j in range(0,5):    
            print("par[%d] = " % j + str(par[j]))
        par = []
            
    if( len(impar) == 5 ):
        for j in range(0,5):
            print("impar[%d] = " % j + str(impar[j]))
        impar = []  


for i in range(0, len(impar)):
     print("impar[%d] = " % i + str(impar[i]))
for i in range(0, len(par)):
     print("par[%d] = " % i + str(par[i]))
