lista = ['zero', 'um', 'dois']

for tentiva in range(3):
    try:
        i = int(input('Idx: '))
        print(lista[i])
    except ValueError:
        print(f'Digite um numero')
    except IndexError:
        print(f'Valor invalido, digite entre 0 e {len(lista) - 1}')
    finally:
        print('Fé')
