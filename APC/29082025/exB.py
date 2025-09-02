import os

# cadastro de produto

# lista de produtos
# contatos serão objetos/dicionários
# @param
# Intenger  - ID do produto e chave primaria
# String    - Nome do produto
# Float     - Preço do produto
products = []

# Execução principal
def main():
    id = 0
    # Loop de execução principal do programa
    while True:
        print(f'-------- Menu --------\n1 - Adicionar produto\n2 - Alterar produto\n3 - Mostrar produtos\n4 - Sair\n----------------------')
        decider = input('Escolha uma opção: ')

        clear_console()
        if decider.strip() == '1': # Adicionar produto
            name = input('Digite o nome do produto: ').strip()
            price = input('Digite o preço do produto: ').strip()
            adicionar_produto(products, name, price)
        elif decider.strip() == '2': # Altera contato
            id = input('Digite o id do produto: ').strip()
            name = input('Digite o nome do produto: ').strip()
            price = input('Digite o preço do produto: ').strip()
            alterar_produto(products,id,name, price)
        elif decider.strip() == '3': # Buscar contato
            mostrar_produtos(products)
        elif decider.strip() == '4': # Sair
            print(f'----------------------\nFim do programa.\n----------------------')
            break
        else:
            print(f'Digite uma opção valida!\n')

# L impa o console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Adiciona um produto na lista
def adicionar_produto(products, name, price):
    try:
        price = float(price)
        if not name or not price: 
            print(f'A criação de contato falhou, tente novamente! \n\nERRO: Nome e preço não podem estar vazio.')
        else:
            id += 1
            product = {
                'id': id,
                'name': name,
                'price': price 
            }
            products.append(product)
            print(f'Produto criado com sucesso!')
    except Exception as err:
        print(f'A criação de produto falhou, tente novamente! \n\nERRO: {err}')

# Exclusão de contato
def alterar_produto(products, id, name, price):
    try:
        for product in products:
            if product['id'] == id:
                price = float(price)
                if not name or not price: 
                    print(f'A alteração de prduto falhou, tente novamente! \n\n ERRO: Nome e preço não podem estar vazio.')
                else:
                    product['name'] = name
                    product['price'] = price
                    print('Produto alterado com sucesso!')
            else:
                print(f'A alteração de produto falhou, tente novamente! \n\nERRO: Produto não encontrado.')
    except Exception as err:
        print(f'A alteração de produto falhou, tente novamente! \n\nERRO: {err}')

# Mostra todos os contatos
def mostrar_produtos(products):
    if len(products) == 0:
        print(f'Sua lista de contatos está vazia!\n')
    else:
        print(f'----------------------')
        for product in products:
            print(f'Produto: {product['name']} \nNúmero: {product['id']}')
        print(f'----------------------')
        
# executo a main depois de carregar todo o código-fonte
if __name__ == "__main__":
    main()