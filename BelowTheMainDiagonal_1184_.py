op = str(input())
soma = 0
i, j = 12, 12;
matrix = [[0 for x in range (i)] for y in range (j) ]

for x in range (i):
    for y in range (j):
       matrix[x][y] = float(input()) 

if( op == "S"):
    for x in range(0, 12):
        for y in range(0, 12):
            if( x > y ):
                soma = soma + matrix[x][y]

if( op == "M"):
    for x in range(0, 12):
        for y in range(0, 12):
            if( x > y ):
                soma = soma + matrix[x][y]
    soma = soma/66

print(round(soma,1))