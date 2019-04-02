while True:
    try:
        X,M = input().split(" ")    
        X = int(X)
        M = int(M)
        if(X == 0 and M == 0):
            break
 
        print(X*M)
    except EOFError:
        break