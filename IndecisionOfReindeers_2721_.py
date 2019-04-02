lista = ['Dasher','Dancer','Prancer','Vixen','Comet','Cupid','Donner','Blitzen','Rudolph'] 
a, b, c, d ,e ,f ,g, h ,i = input().split(" ")
soma = int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i)
resto = soma % 9
print(lista[resto-1])