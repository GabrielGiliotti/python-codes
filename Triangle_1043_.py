A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)

if(A+B > C and B+C > A and A+C > B):
	print("Perimetro = %.1f" % (A+B+C))
else:
	print("Area = %.1f" % (((A+B)*C)/2))