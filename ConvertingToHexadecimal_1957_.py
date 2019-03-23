#hexadecimal
V = int(input())
lista = []

V = hex(V)
lista.extend(V.split('0x'))
print(lista[1].upper())
