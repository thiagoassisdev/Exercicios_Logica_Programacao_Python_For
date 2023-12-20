'''•	Escreva um programa para calcular o fatorial de um número n digitado pelo usuário.
 Por exemplo: n = 5     fatorial = 5 x 4 x 3 x 2 x 1 = 120. OBS: utilize o “for”.'''

n = int(input("Digite o numero do fatorial que deseja:"))
fat = 1

for i in range(1, n+1):
    fat = fat * i

print(f"fatorial de {n} é {fat}")