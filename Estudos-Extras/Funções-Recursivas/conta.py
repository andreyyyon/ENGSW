lista = [30, 20, 10, 5]

def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:]) # soma 1 com a contagem do restante da lista