#Funcao Recursiva
def function_rec( N ):
    if( N == 0 ):
        return 0
    if( N == 1 ):
        return (1/6)
    else:
        return 1/(6+(function_rec(N-1)))    

N = int(input())
x = 3 + function_rec(N)
print("%.10f" % float(x))