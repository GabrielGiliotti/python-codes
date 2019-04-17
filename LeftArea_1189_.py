
mat = [[0 for i in range (12)] for j in range (12)]
e = input()
for i in range(12):
    for j in range(12):
        mat[i][j] = float(input())

soma = 0 
if( e == 'S'):
    for i in range(12):
        for j in range(12):
            if(( i >= 1 and i <= 10 ) and ( j >= 0 and j <= 4 ) and (i+j<=10) and (i-j>=1) ):
                soma = soma + mat[i][j]

if( e == 'M'):
    for i in range(12):
        for j in range(12):
            if(( i >= 1 and i <= 10 ) and ( j >= 0 and j <= 4 ) and (i+j<=10) and (i-j>=1) ):
                soma = soma + mat[i][j]
    soma = soma/30


print("%.1f" % soma)