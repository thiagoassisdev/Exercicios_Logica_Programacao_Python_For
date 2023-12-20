"""
Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 devem ser somados.
Escreva o valor final da soma efetuada.
"""
soma=0

for i in range(1,11):
    num=int(input("Informe o numero:"))
    if (num < 40):
        soma += num
print(f"A soma dos numero inferiores a 40 é de {soma}")
