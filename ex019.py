import random

n1 = input("Nome do primeiro aluno: ")
n2 = input("Nome do segundo aluno: ")
n3 = input("Nome do terceito aluno: ")
n4 = input("Nome do quarto aluno: ")

alunos = [n1, n2, n3, n4]

sorteado = random.choice(alunos)

print(f"O aluno sorteado foi {sorteado}!")