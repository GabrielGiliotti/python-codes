N = int(input())

Ano = int(N / 365)
Resto = (N % 365)
Meses = int(Resto / 30)
Dias = Resto % 30

print(Ano, "ano(s)")
print(Meses, "mes(es)")
print(Dias, "dia(s)")