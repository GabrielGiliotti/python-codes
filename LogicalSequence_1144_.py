N = int(input())
num = 1

for i in range (1, N+1):
    print(num, num*i, num*i*i)
    print(num, (num*i)+1, (num*i*i)+1)
    num += 1
