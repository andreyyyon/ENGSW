lista = [30, 20, 10, 5]

def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1] # retorna o maior entre os dois elementos
    sub_max = maximo(lista[1:]) # chama a função recursivamente com a lista sem o primeiro elemento
    return lista[0] if lista[0] > sub_max else sub_max # retorna o maior entre o primeiro elemento da lista e o maior dos outros elementos

