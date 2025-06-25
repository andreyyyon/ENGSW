# Questão 1: Elaborar um programa em Python que efetue o cálculo do fatorial de um número inteiro 
# informado pelo usuário.

x = int(input("Preencha um valor inteiro para realizar a Fatorial: "))
calc = 1

for z in range(1, x + 1):
    calc *= z

print(calc)