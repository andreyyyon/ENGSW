#1
numeros = [1 , 2, 3]
numeros.append([4, 5])
print(numeros)
# [1, 2, 3, [4, 5]]

#2
# print(numeros[4])
# array out of bounds 

#3
# Listas podem ser manipuldas a todo momento, a tupla pelo contrário não pode ser alterada após declarada
# a tupla pode apenas ser clonada e gerada uma nova com base nessa incial.

#4
tupla = (10, 20, 30)
print(tupla[1])
# 20

#5
notas = {
    'Ana': 8.5,
    'Bruno': 6.0,
    'Carlos': 9.0
}
print(notas['Bruno'])

#6 
Estados = {
    'RS': [
        'Gravatai',
        'Pelotas',
        'Erechim'
    ],
    'SC': [
        'Joinville',
        'Jaraguá',
        'Blumenau'
    ],
    'PR': [
        'Curitiba',
        'Toledo',
        'Maringá'
    ]
}


#7
print(Estados['SC'][0])

#8
names = []
for x in range(5):
    while True:
        name = input('Digite um nome: ')
        if not name:
            print('Digite um nome valido!')
        else:
            names.append(name)
            break
tuplaNames = tuple(names)
print(tuplaNames)

#9 Feito da forma mais simples possivel e sem validações
nomes = []

while True:
    print("\n--- Menu ---")
    print("1 - Adicionar nome")
    print("2 - Remover nome")
    print("3 - Alterar nome")
    print("4 - Mostrar lista de nomes")
    print("5 - Sair")
    print("------------")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Digite o nome que deseja adicionar: ")
        nomes.append(nome)
        print(f"'{nome}' foi adicionado com sucesso.")
    
    elif opcao == '2':
        if nomes:
            nome = input("Digite o nome que deseja remover: ")
            if nome in nomes:
                nomes.remove(nome)
                print(f"'{nome}' foi removido com sucesso.")
            else:
                print(f"'{nome}' não foi encontrado na lista.")
        else:
            print("A lista está vazia. Não há nomes para remover.")

    elif opcao == '3':
        if nomes:
            nome_antigo = input("Digite o nome que deseja alterar: ")
            if nome_antigo in nomes:
                novo_nome = input(f"Digite o novo nome para '{nome_antigo}': ")
                indice = nomes.index(nome_antigo)
                nomes[indice] = novo_nome
                print(f"'{nome_antigo}' foi alterado para '{novo_nome}' com sucesso.")
            else:
                print(f"'{nome_antigo}' não foi encontrado na lista.")
        else:
            print("A lista está vazia. Não há nomes para alterar.")
    
    elif opcao == '4':
        if not nomes:
            print("A lista de nomes está vazia.")
        else:
            print("\n--- Lista de Nomes ---")
            for i, nome in enumerate(nomes):
                print(f"{i+1}. {nome}")
            print("---------------------\n")
            
    elif opcao == '5':
        print("Saindo do programa. Até mais!")
        break
        
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 5.")