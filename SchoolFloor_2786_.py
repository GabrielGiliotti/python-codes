#OBI
L = int(input())
C = int(input())

numLaj1 = 0
numLaj2 = 0

L2 = L - (2*0.5)  
C2 = C - (2*0.5)

numLaj2 = 2*(L2+C2)
numLaj1 = ((L*C)-((4*0.125)+(((L2*0.25)+(C2*0.25))*2)))/0.5

print(int(numLaj1))
print(int(numLaj2))