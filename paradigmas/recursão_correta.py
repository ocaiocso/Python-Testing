'''
par = lambda x: x if x % 2 == 0 else x+1
somar = lambda x, y: x + y
print(somar(par(int(input("num1: "))),(par(int(input("num2: "))))))
print(maior_dois(int(input("num1: ")), int(input("num2: "))))

maior_dois = lambda x, y: x if x>y else y
maior_tres = lambda x, y, z: maior_dois(x,y) if x>y else maior_dois(y,z)

print(maior_tres(int(input("num1: ")), int(input("num2: ")), int(input("num3: "))))
'''

adc = lambda x,y: x+y
intervalo = lambda x, y: adc(x,intervalo(x+1,y)) if x<y-1 else adc(x, y)
print(intervalo(int(input("num1: ")), int(input("num2: "))))