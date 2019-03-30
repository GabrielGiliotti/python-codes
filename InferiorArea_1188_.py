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
            if( x>=7 and (((y>=1 and y<=5) and (x+y>=12 and x+y<=16)) or ((y>=6 and y<=10) and (x-y<=5 and x-y>=1)))):
                soma = soma + matrix[x][y]

if( op == "M"):
    for x in range(0, 12):
        for y in range(0, 12):
            if( x>=7 and (((y>=1 and y<=5) and (x+y>=12 and x+y<=16)) or ((y>=6 and y<=10) and (x-y<=5 and x-y>=1)))):
                soma = soma + matrix[x][y]
    soma = soma/30

print(round(soma,1))
