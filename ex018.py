from math import sin, cos, tan, radians, ceil
a = float(input('Digite o ângulo que você deseja: ')) 
seno = sin(radians(a))     
coseno = cos(radians(a))
tangente = tan(radians(a))
print(f'O seno de {a} é {seno:.2f}')
print(f'O coseno de {a} é {coseno:.2f}')
print(f'A tangente de {a} é {tangente:.2f}')