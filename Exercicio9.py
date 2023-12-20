'''•	Escreva um programa que calcule o somatório de todos os números pares em um
intervalo definido pelo usuário. Ex: para inicio = 2 e fim = 10 o somatório é 2+4+6+8+10.
 OBS: utilize o “for”.'''

inicio = int(input("Digite o inicio do intervalo:"))
fim = int(input("Digite o fim do intervalo:"))
soma_pares = 0

for i in range(inicio,fim+1):
    if (i % 2 == 0):
        soma_pares+=i

print(f"A soma dos pares entre {inicio} e {fim} é {soma_pares}")