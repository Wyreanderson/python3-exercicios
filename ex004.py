x = input('Digite algo: ')

print(f'O timpo primitivo desse valor é {type(x)}')

#print(f'O tipo primitivo desse valor é {wyre.__class__}')
#segunda forma de saber a classe de uma "str"

print(f'Só tem espaços? {x.isspace()}')

print(f'É um número? {x.isnumeric()}')

print(f'É alfabético? {x.isalpha()}')

print(f'É alfanumérico? {x.isalnum()}')

print(f'Está em maiúscula? {x.isupper()}')

print(f'Está em minuscula? {x.islower()}')

print(f'Está capitalizada? {x.istitle()}')