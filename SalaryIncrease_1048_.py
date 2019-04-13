# 0 - 400.00  15%
# 400.01 - 800.00 12%
# 800.01 - 1200.00  10%
# 1200.01 - 2000.00 7%
# 2000.01 +  4%
N = float(input())
if( N >= 0.00 and N <= 400.00 ):
    print("Novo salario: %.2f" % (N*1.15), end="\n")
    print("Reajuste ganho: %.2f" % (N*0.15), end="\n")
    print("Em percentual: 15 %")
elif( N >= 400.01 and N <= 800.00 ):
    print("Novo salario: %.2f" % (N*1.12), end="\n")
    print("Reajuste ganho: %.2f" % (N*0.12), end="\n")
    print("Em percentual: 12 %")

elif( N >= 800.01 and N <= 1200.00 ):
    print("Novo salario: %.2f" % (N*1.10), end="\n")
    print("Reajuste ganho: %.2f" % (N*0.10), end="\n")
    print("Em percentual: 10 %")

elif( N >= 1200.01 and N <= 2000.00 ):
    print("Novo salario: %.2f" % (N*1.07), end="\n")
    print("Reajuste ganho: %.2f" % (N*0.07), end="\n")
    print("Em percentual: 7 %")

elif( N >= 2000.01 ):
    print("Novo salario: %.2f" % (N*1.04), end="\n")
    print("Reajuste ganho: %.2f" % (N*0.04), end="\n")
    print("Em percentual: 4 %")
