while True:
    try:
        H = input()
        hora = int(H[0])    #feira abre as 8:00
        minuto = int(H[2])  # splitar por : (dois pontos) é mais eficiente
        minuto2 = int(H[3])
        hora = hora + 1     
        
        # H = input().split(":")
        # lista = list(map(int, input().split(":")))
        # print(lista)  check

        if( hora - 8 < 0):
            print("Atraso maximo: 0")
        else:
            if(minuto == 0 and hora-8 <= 0):
                print("Atraso maximo: "+str(H[3]))
            else:
                if( hora - 8 == 0 ):
                    print("Atraso maximo: "+str(H[2])+str(H[3]))
                else:
                    totalmin = (hora - 8)*60 + (10*int(H[2])) + int(H[3])
                    print("Atraso maximo: "+str(totalmin))
               
    except EOFError:
        break