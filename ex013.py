salario = float(input("Qual o salario atual do funcionario? R$"))

aumento = salario+(salario * 15 / 100)

print(f"Um funcionario que recebe um salario de R${salario} com um aumento de 15% passa a receber R${aumento:.2f}.")