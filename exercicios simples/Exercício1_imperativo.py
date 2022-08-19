list = [int(x) for x in input().split()]
print("Maior: ", max(list))
print("Menor: ", min(list))
print("Media: ", sum(list)/len(list))
"""
maior = lambda x : max(x)
menor = lambda x : min(x)
media =  lambda x : sum(x)/len(x)
exibicao = lambda x : print(str(maior(x))+"\n"+str(menor(x))+"\n"+str(media(x)))
exibicao ([int(x) for x in input().split()])
"""


string = input()
print(string.upper())



