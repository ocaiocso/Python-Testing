from functools import reduce

maior = lambda x,y : sorted([x,y])

maior_str = list(map(str,maior(20,10)))

dobro_maior = list(map(lambda x : 2*x,maior(20,10)))
soma_maior = 10
soma_maior  = reduce(lambda x,y: x+y,maior(20,10),soma_maior)

filtro_maior_10 = list(filter(lambda x: x>10,maior(20,10)))

print(maior_str)
print(dobro_maior)
print(soma_maior)
print(filtro_maior_10)
