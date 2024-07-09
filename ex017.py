from math import sqrt
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
h =  sqrt(c1 ** 2 + c2 ** 2) 
print(f'A hipotenusa tem valor {h:.2F}')