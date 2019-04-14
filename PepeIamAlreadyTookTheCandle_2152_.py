N = int(input())
for i in range(N):
    H,M,S = input().split(" ")
    if( int(S) == 0 ):
        if( int(H) >= 10 and int(M) >= 10 ):    
            print(H+":"+M+" - A porta fechou!")
        if( int(H) >= 10 and int(M) < 10 ):
            print(H+":0"+M+" - A porta fechou!")
        if( int(H) < 10 and int(M) >= 10 ):
            print("0"+H+":"+M+" - A porta fechou!")
        if( int(H) < 10 and int(M) < 10 ):
            print("0"+H+":0"+M+" - A porta fechou!")
    else:
        if( int(H) >= 10 and int(M) >= 10 ):    
            print(H+":"+M+" - A porta abriu!")
        if( int(H) >= 10 and int(M) < 10 ):
            print(H+":0"+M+" - A porta abriu!")
        if( int(H) < 10 and int(M) >= 10 ):
            print("0"+H+":"+M+" - A porta abriu!")
        if( int(H) < 10 and int(M) < 10 ):
            print("0"+H+":0"+M+" - A porta abriu!")
