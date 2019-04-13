import math
A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
delta = (B*B)-(4*A*C)
if( delta < 0 or A == 0 ):
    print("Impossivel calcular", end="\n")
else:
    R1 = ((-1)*B + math.sqrt(delta))/(2*A)
    R2 = ((-1)*B - math.sqrt(delta))/(2*A)
    print("R1 = %.5f" % R1, end="\n")
    print("R2 = %.5f" % R2, end="\n")
