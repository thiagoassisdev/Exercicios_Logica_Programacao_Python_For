'''•	Desenvolva um programa que receba um número inteiro positivo  n. Exiba na tela a tabuada de multiplicação (0 ao 10) para o número informado pelo usuário.
Conforme exemplo abaixo:

Digite um número inteiro positivo: 5
5 x 0=0
5 x1 =5
5 x2=10
5 x3=15
…
5 x10=50
'''

num_tab = int(input("Digite o numero da tabuada que deseja:"))

for cont in range(11):
    tab = num_tab * cont
    print(f"{num_tab} x {cont} = {tab}")