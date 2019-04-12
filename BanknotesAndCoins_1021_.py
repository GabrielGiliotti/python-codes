R, C = input().split(".")
R = int(R)
C = int(C)
cem = R / 100
cinq = (R % 100)/ 50
vint = ((R % 100) % 50)/20
dez = (((R % 100) % 50) % 20) / 10
cinc = ((((R % 100) % 50) % 20) % 10)/ 5
dois = (((((R % 100) % 50) % 20) % 10) % 5)/2
UmRe = ((((((R % 100) % 50) % 20) % 10) % 5) % 2)
CinqCent = (C % 100)/50
VCinCent = ((C % 100) % 50)/25
DezCent = (((C % 100) % 50) % 25) / 10
CincCent = ((((C % 100) % 50) % 25) % 10)/5
UmCent = ((((( C % 100) % 50) % 25) % 10) % 5)
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinq)
print("%d nota(s) de R$ 20.00" % vint)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinc)
print("%d nota(s) de R$ 2.00" % dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % UmRe)
print("%d moeda(s) de R$ 0.50" % CinqCent)
print("%d moeda(s) de R$ 0.25" % VCinCent)
print("%d moeda(s) de R$ 0.10" % DezCent)
print("%d moeda(s) de R$ 0.05" % CincCent)
print("%d moeda(s) de R$ 0.01" % UmCent)