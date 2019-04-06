import math
while True:
    try:
        e = input().split(" ")
        if( e[len(e)-1] == '0'):
            break
        A = int(e[0])
        B = int(e[1])
        C = int(e[2])

        AreaT = A*B /(C/100)
        lado = int(math.sqrt(AreaT))
        print(lado)
    except EOFError:
        break
