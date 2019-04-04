lista = [[1,4.00],[2,4.50],[3,5.00],[4,2.00],[5,1.50]]

X,Y = input().split(" ")
X = int(X)
Y = int(Y)

total = 0
for i in range(0,5):
    if( lista[i][0] == X ):
        total = total + lista[i][1]
        total = total*Y

print("Total: R$ %.2f" % total)