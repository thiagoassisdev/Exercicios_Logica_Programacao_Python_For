'''
Desenvolva um programa que receba:

o	taxa de abatimento em porcentagem;
o	número de prestações;
o	valor da primeira prestação.

Seu programa deverá exibir na tela os valores das prestações decrescente dado que a cada mês o valor da prestação diminui
do valor da prestação do mês anterior(utilize a taxa de abatimento fornecida pelo usuário para realizar esse cálculo).
OBS: utilize o “for”.
'''

taxa_abatimento = int(input("Informe a taxa de abatimento em porcetagem: "))
numero_prestacoes = int(input("Informe o numero de prestações: "))
val_primeira_prestacao = float(input("Informe o valor da primeira prestação: "))


for prest in range(numero_prestacoes):
    if (prest == 0):
        print(f"Prestação {prest+1}: R${val_primeira_prestacao:.2f} ")
        valor_prest = val_primeira_prestacao
    else:
        valor_prest = valor_prest - (valor_prest * taxa_abatimento/100)
        print(f"Prestação {prest+1}: R${valor_prest:.2f}")













'''
taxa_abatimento = float(input("Digite a taxa de abatimento:"))
nro_prest = int(input("Digite o quantidade de prestações:"))
primeira_prest = float(input("Digite o valor da primeira prestação:"))

for prest in range (nro_prest):
    if (prest == 0): #primeira interação do for
        print(f"Prestação{prest+1}: {primeira_prest:.2f}")
        valor_prest = primeira_prest
    else:
        valor_prest = valor_prest - (valor_prest * taxa_abatimento/100)
        print(f"Prestação{prest + 1}: {valor_prest:.2f}")
'''