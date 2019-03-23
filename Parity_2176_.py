#Se S tem um numero PAR de bits de valor 1, o bit B adicionado no final eh 0
#Se S tem um numero IMPAR de bits de valor 1, o bit B adicionado no final eh 1

String = input()
cont = String.count('1')

if(cont % 2 == 0):
    print(String+"0")
else:
    print(String+"1")
