'''
Desenvolva um programa para calcular a média salarial dos funcionários da empresa XXX, para isso seu programa deverá solicitar o nome
e salário dos 5 funcionários que trabalham nessa empresa. Ao final seu programa deverá calcular a média dos salários e exibir na tela
as seguintes informações:
(use 2 casas decimais na exibição dos números)

o	A média salarial dos funcionários da empresa XXX é _______
o	O nome e o salário do funcionário que recebe o menor salário
o	O nome e o salário do funcionário que recebe o maior salário
'''


nome_empresa = input("Informe o nome da empresa: ")

soma_salario = 0

for i in range(5):
    nome = input("Informe o nome do funcionário: ")
    salario = float(input("Informe o salario do funcionario: "))
    soma_salario += salario/5
    if (i == 0):
        maior_salario = salario
        nome_maior_salario = nome
        menor_salario = salario
        nome_menor_salario = nome
    else:
        if (salario > maior_salario):
            maior_salario = salario
            nome_maior_salario = nome
        if (salario < menor_salario):
            menor_salario = salario
            nome_menor_salario = nome

print(f"A média salarial dos funcionários da empresa {nome_empresa} é de R$:{soma_salario:.2f}")
print(f"O {nome_menor_salario} que recebe o salario de R$:{menor_salario:.2f} é o funcionário que recebe o menor salário.")
print(f"O {nome_maior_salario} que recebe o salario de R$:{maior_salario:.2f} é o funcionário que recebe o maior salário.")






