# tratar todas as possibilidades de PAR ou IMPAR
T = int(input())
venc = []
for i in range(T):

    frase=input().split()
    jogador1=str(frase[0])
    escolha1=str(frase[1].lower())
    jogador2=str(frase[2])
    escolha2=str(frase[3].lower())

    nums=input().split()
    num1=int(nums[0])
    num2=int(nums[1])
    soma=int(num1+num2)

    if( soma % 2 == 0 and escolha1 == 'par'):
        venc.append(jogador1)
    if( soma % 2 != 0 and escolha1 == 'par'):
        venc.append(jogador2)
    if( soma % 2 == 0 and escolha1 == 'impar'):
        venc.append(jogador2)
    if( soma % 2 != 0 and escolha1 == 'impar'):
        venc.append(jogador1)

for i in range(0, T):
    print(venc[i])





