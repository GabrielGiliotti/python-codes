while True:
    try:
        N, M = input().split(" ")
        N = int(N)
        M = int(M)
        
        if(M == 0 and N == 0):
            break 
        
        troco = M - N
        lista = [2,5,10,20,50,100]
        cont = 0

        if( troco >= 100 ):
            troco = troco - 100
            lista[5] = 0

        if( troco >= 50 ):
            troco = troco - 50
            lista[4] = 0

        if( troco >= 20 ):
            troco = troco - 20
            lista[3] = 0

        if( troco >= 10 ):
            troco = troco - 10
            lista[2] = 0

        if( troco >= 5 ):
            troco = troco - 5
            lista[1] = 0

        if( troco >= 2 ):
            troco = troco - 2
            lista[0] = 0       


        for i in range (0,6):
	        if(lista[i] == 0):
	            cont += 1

        if( cont == 2 and troco == 0 ):
            print("possible")
        else:
            print("impossible")  
    
    except EOFError:
        break