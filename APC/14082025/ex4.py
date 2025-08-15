# 4 – F.U.P que leia números até que o usuário digite 0. Armazene os números 
# em uma lista e, ao final, mostre a soma total.

lista = []
x = 0

while True:
    x += 1
    while True:
        z = input(f'{x}º número: ')
        try:
            z = int(z)
            if z != 0:
                lista.append(z)
            break
        except:
            print('Digite um número valido!')
    if z == 0:
        break

# já vi essa recursiva também pra esse
def soma(lista):
    if lista == []: 
        return 0
    return lista[0] + soma(lista[1:]) # soma o primeiro elemento da lista com a soma do restante da lista

print(soma(lista))

# com loop
soma = 0
for x in lista:
    soma += x

print(f'Soma da lista: {soma}')