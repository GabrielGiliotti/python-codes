def func_rec(num):
    if( num == 0 ):
        return num
    else:
        return 1/(2+func_rec(num-1)) 

N = int(input())
soma = 1 + func_rec(N)
print("%.10f" % soma)