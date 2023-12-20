"""
Escreva um programa que calcule a soma de todos os números pares entre 1 e 20.
"""

soma=0

for cont in range (1,21):
    if (cont % 2 == 0):
        soma = soma+cont

print(f"A soma dos numeros pares de 1 até 20 é de {soma}")



