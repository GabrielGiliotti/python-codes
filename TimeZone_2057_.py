# TimeZone (2057)
S, T, F = input().split()

S = int(S)
T = int(T)
F = int(F)

soma = S + T + F

if( soma >= 24 ):
	soma = soma - 24

if( soma < 0 ):
    soma = soma + 24	

print(soma)