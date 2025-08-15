# 5 – F.U.P que leia as notas de alunos até que o usuário digite uma nota 
# negativa. Armazene as notas em uma lista. No final do programa deverá 
# mostrar:
# - A soma total das notas
# - A média das notas
# - A maior e menor nota


lista = []
x = 0

while True:
    x += 1
    while True:
        z = input(f'{x}º nota: ')
        try:
            z = int(z)
            if z > 0:
                lista.append(z)
            break
        except:
            print('Digite um número valido!')
    if z < 0:
        break

soma = 0
y = lista[0]
z = lista[0]
for x in lista:
    soma += x
    if x > y:
        y = x
    if x < z:
        z = x

media = soma / len(lista)

print(f'Soma da lista de notas: {soma}')
print(f'Média da lista de notas: {media}')
print(f'Maior número da lista de notas: {y}')
print(f'Menor número da lista de notas: {z}')
