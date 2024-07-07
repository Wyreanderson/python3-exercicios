a = float(input('Dígite a Altura da área a ser pintada: '))

l = float(input('Dígite a Largura da área a ser pintada: '))

area = a*l

tinta = (area/2)

print(f"Sua parede tem a dimensao de {a}x{l} e sua area e de {area}m2.")
print(f"Para pintar essa parede, voce precisara de {tinta:.1f}l de tinta.")