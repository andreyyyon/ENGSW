# 1 – F.U.P que solicite ao usuário digitar números e armazene-os em uma lista. 
# Pode ser 5 números. E depois pergunte ao usuário qual número deseja 
# procurar e diga se ele está ou não na lista. Use if e else.

lista = []

print('Digite cinco números diferentes:')

for x in range(5):
    while True:
        z = input(f'{x + 1}º número: ')
        try:
            z = int(z)
            if z not in lista:
                lista.append(z)
                break
            else:
                print('Digite um valor que não se repita!')
        except:
            print('Digite um número válido!')

try:
    idx = int(input('Qual valor você deseja procurar? '))
    if idx in lista:
        print(f'Sim, {idx} está na lista.')
    else:
        print(f'Não, {idx} não está na lista.')
except:
    print('Digite um número válido.')
