N1, N2, N3, N4 = input().split(" ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)
Media = ((2*N1)+(3*N2)+(4*N3)+(N4))/10

print("Media: %.1f" % Media)
if(Media >= 7):
	print("Aluno aprovado.")
elif(Media < 5):
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	N5 = float(input())
	print("Nota do exame: %.1f" % N5)
	Media = (Media + N5)/2
	if(Media >= 5):
		print("Aluno aprovado.")
		print("Media final: %.1f" % Media)
	else:
		print("Aluno reprovado.")
		print("Media final: %.1f" % Media)