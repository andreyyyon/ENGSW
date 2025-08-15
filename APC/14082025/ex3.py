# 3 – F.U.P que peça a idade de várias pessoas e classifique-as como "Criança" 
# (0 a12), "Adolescente" (13 a 17), "Adulto" (18 a 59) ou "Idoso" (60+). Use 
# funções, if/elif/else e listas. No final a saída seria assim:

# vou fazer para cinco pessoas mas poderia usar um loop de while pe inserir quantas eu quisesse
lista = []
x = 0

print('Digite zero para finalizar a lista.')
while True:
    x = x + 1
    while True:
        z = input(f'{x}º pessoa: ')
        try:
            z = int(z)
            if z != 0:
                lista.append(z)
            break
        except:
            print('Digite um número valido!')
    if z == 0:
        break


for x in lista:
    if 13 > x:
        print(f'Idade {x}: Criança')
    elif 18 > x > 12:
        print(f'Idade {x}: Adolescente')
    elif 60 > x > 17:
        print(f'Idade {x}: Adulto')
    else:
        print(f'Idade {x}: Idoso')
