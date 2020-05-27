H1, H2 = input().split(" ")
H1 = int(H1)
H2 = int(H2)

count = 24;
if (H1 >= H2):
	count = count - H1 + H2
	print("O JOGO DUROU %d HORA(S)" % count)
else:
	count = H2 - H1
	print("O JOGO DUROU %d HORA(S)" % count)