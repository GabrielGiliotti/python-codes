A, B, C = input().split(" ")
A = int(A)
B = int(B)
C = int(C)

# pelo menso uma viagem e no maximo tres, saber se conseguimos viajar no teḿpo e voltar para onde estamos
# Uma viagem nunca volta para o presente
# duas viagens podem voltar se tiverem um mesmo tempo
# tres viagens , duas delas tem que ser a soma da tarceira

flag1 = 0  
flag2 = 0

if( A+B == C or A+C == B or B+C == A ):
    flag1 = 1
if( A == B or A == C or B == C):
    flag2 = 1

if(flag1 == 1 or flag2 == 1 ):
	print("S")
else:
    print("N")	