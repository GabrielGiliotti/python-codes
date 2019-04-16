# 1 impeachement    -    0 nao impeachement 
while True:
    try:
        N = int(input())
        e = input().split(" ")
        cont = 0
        for i in range(N):
            if( e[i] == '1'):
                cont += 1  
        if( cont >= ((2/3)*N) ):
            print("impeachment") 
        else:
            print("acusacao arquivada")
    except EOFError:
        break