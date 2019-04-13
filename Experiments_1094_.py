N = int(input())
Coelho = 0
Rato = 0
Sapo = 0
for i in range(N):
    e = input().split(" ")
    if(e[1] == 'C'):
        Coelho = Coelho + int(e[0])
    if(e[1] == 'R'):
        Rato = Rato + int(e[0])
    if(e[1] == 'S'):
        Sapo = Sapo + int(e[0])

print("Total: %d cobaias" % (Rato+Sapo+Coelho))
print("Total de coelhos: %d" % Coelho)
print("Total de ratos: %d" % Rato)
print("Total de sapos: %d" % Sapo)
print("Percentual de coelhos: %.2f" % ((Coelho/(Rato+Sapo+Coelho))*100) + " %")
print("Percentual de ratos: %.2f" % ((Rato/(Rato+Sapo+Coelho))*100) + " %")
print("Percentual de sapos: %.2f" % ((Sapo/(Rato+Sapo+Coelho))*100) + " %")
