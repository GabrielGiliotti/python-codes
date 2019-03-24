# L = 1 e C = 1 --> 1

# 1 Branco
# 0 Preto

L = int(input())
C = int(input())

if( L == C ):
    print("1")

elif((L % 2 == 0 and C % 2 == 0)):
    print("1")

elif( (L % 2 != 0 and C % 2 == 0) or (L % 2 == 0 and C % 2 != 0) ):
    print("0")

elif( (L % 2 != 0 and C % 2 != 0) ):
    print("1")
