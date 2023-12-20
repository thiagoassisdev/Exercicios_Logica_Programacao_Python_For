"""
Escreva um programa que faça a leitura das notas dos 3 checkpoints de 15 alunos e mostre a
média dos checkpoints para cada aluno.
"""

for i in range(1,16):
    cp1=int(input("Informe a nota do primeiro cp: "))
    cp2=int(input("Informe a nota do segundo cp: "))
    cp3=int(input("Informe a nota do terceiro cp: "))
    media=(cp1+cp2+cp3)/3
    print(f"A media das notas dos 3 checkpoints é de {media:.1f}")

