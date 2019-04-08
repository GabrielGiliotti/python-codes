lista = []
cont = 0
soma = 0
for i in range(0,6):
    lista.append(float(input()))
    if(lista[i] > 0):
        cont += 1
        soma = soma + lista[i] 
    
media = soma/cont   
print(cont, "valores positivos")
print("%.1f" % media)	