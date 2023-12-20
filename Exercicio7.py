'''Escreva um algoritmo que solicite dois números e devolva quantos pares e
ímpares há entre esses dois números. Exemplo: entre 7 e 10 há 2 números pares
e 2 números ímpares'''

num1 = int(input("Informe o inicio do intervalo:"))
num2 = int(input("Informe o fim do intervalo: "))
conta_pares = 0
conta_impares = 0

for i in range(num1, num2+1):
    if (i % 2 == 0):
        conta_pares += 1
    else:
        conta_impares += 1

print(f" Entre o numero {num1} e o numero {num2} há {conta_pares} numero pares.")
print(f" Entre o numero {num1} e o numero {num2} há {conta_impares} numero pares.")




