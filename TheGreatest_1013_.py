A,B,C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)
MaiorAB = (A+B+abs(A-B))/2
Maior = (MaiorAB+C+abs(MaiorAB-C))/2
print(int(Maior),"eh o maior", end="\n")