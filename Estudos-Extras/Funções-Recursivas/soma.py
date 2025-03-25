lista = [30, 20, 10, 5]

def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:]) # soma o primeiro elemento da lista com a soma do restante da lista

# lista[1:] -> cria uma nova lista com todos os elementos da original, exceto o primeiro elemento