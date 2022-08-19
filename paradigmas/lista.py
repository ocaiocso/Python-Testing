lista=[1,2,3,4]

print(lista)

new_num=int(input("Digite um número:"))
maior = lista[0]
lista.append(int(new_num))
for x in lista:
    if maior < x:
        maior = x


print("Maior: ", maior)