# 2 – F.U.P que receba uma lista de números. (Primeiramente faça uma lista) O 
# Programa deverá retornar o maior número da lista. Podem ser 5 números. Use 
# uma estrutura de repetição para percorrer os elementos

lista = [30, 40, 50, 70, 10]

# Vi uma função recursiva no livro Entendendo Algoritmos da Aditya Y. Bhargava, essa função vai ser muito mais rapida conforme a lista for maior 
def maximo(lista):
    if len(lista) == 2:
        # retorna o maior entre os dois elementos (caso base)
        return lista[0] if lista[0] > lista[1] else lista[1] 
    # chama a função recursivamente com a lista sem o primeiro elemento (reparto a lista em uma menor até ficar com o tamanho do caso base)
    sub_max = maximo(lista[1:]) 
    # retorna o maior entre o primeiro elemento da lista e o maior dos outros elementos (retorno o menor numero dos casos)
    return lista[0] if lista[0] > sub_max else sub_max 

print(maximo(lista))

# Fazendo com loop
y = 0
for x in lista:
    if x > y:
        y = x

print(f'O maior número da lista é {y}')