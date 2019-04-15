while True:
    try:
        cont = 0
        N,I = input().split(" ")
        N = int(N)
        I = int(I)
        for i in range(N):    
            ID,J = input().split(" ")
            if( int(ID) == I and int(J) == 0 ):
                cont += 1
        print(cont)
    except EOFError:
        break