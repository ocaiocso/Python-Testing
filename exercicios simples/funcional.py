par = lambda x: x % 2 == 0
impar = lambda x: x % 2 != 0

lista = [int(x) for x in input().split()]
print(par(lista),impar(lista))