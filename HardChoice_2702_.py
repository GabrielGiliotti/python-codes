Ca, Ba, Pa = input().split(" ")
Cr, Br, Pr = input().split(" ")

Ca = int(Ca)
Ba = int(Ba)
Pa = int(Pa)
Cr = int(Cr)
Br = int(Br)
Pr = int(Pr)

qtd = 0
if( Cr > Ca ):
    qtd += Ca - Cr

if( Br > Ba ):
    qtd += Ba - Br

if( Pr > Pa ):
    qtd += Pa - Pr 

print(qtd*(-1))       