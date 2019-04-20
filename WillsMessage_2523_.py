while True:
    try:
        alfabeto = []
        alfabeto.extend(input())
        N = int(input())
        text = []
        out = ""
        text.extend(input().split(" "))
        for i in range(N):
            text[i] = alfabeto[int(text[i])-1]
        print(out.join(text))
    except EOFError:
        break

# Era pra funcionar, pois faz o mesmo que acima
'''while True:
    try:
        letras = input()
        N = int(input())
        palavra = input().split(" ")
        palavra = list(map(int,palavra))
        out = [] 
        for i in range(N):
            out.append(letras[palavra[i]-1])
        for i in range(len(out)):
            print(str(out[i]), end="\0")
        print()        
    except EOFError:
        break
'''
