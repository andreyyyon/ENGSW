import os

# gerenciador de contatos

# lista de contatos
# contatos serão objetos/dicionários
# @param
# String    - Nome do contato
# Intenger  - Número do contato e chave primaria
contacts = []

# Execução principal
def main():
    # Loop de execução principal do programa
    while True:
        print(f'-------- Menu --------\n1 - Adicionar contato\n2 - Remover contato\n3 - Buscar contato\n4 - Mostrar contatos\n5 - Sair\n----------------------')
        decider = input('Escolha uma opção: ')

        clear_console()
        if decider.strip() == '1': # Adicionar contato
            name = input('Digite o nome do contato: ').strip()
            number = input('Digite o número de telefone: ').strip()
            adicionar_contato(contacts, name, number)
        elif decider.strip() == '2': # Remover contato
            number = input('Qual contato deseja excluir? ').strip()
            remover_contato(contacts, number) 
        elif decider.strip() == '3': # Buscar contato
            number = input('Qual contato deseja buscar? ').strip()
            buscar_contato(contacts, number)
        elif decider.strip() == '4': # Mostrar contatos
            mostra_contatos(contacts)
        elif decider.strip() == '5': # Sair
            print(f'----------------------\nFim do programa.\n----------------------')
            break
        else:
            print(f'Digite uma opção valida!\n')



# L impa o console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Adiciona um contato na lista
def adicionar_contato(contacts, name, number):
    try:
        if not name or not number: 
            print(f'A criação de contato falhou, tente novamente! \n\nERRO: Nome e telefone não podem estar vazio.')
        elif any(x['number'] == number for x in contacts):
            print(f'A criação de contato falhou, tente novamente! \n\nERRO: Telefone já cadastrado.')
        else:
            contact = {
                'name': name,
                'number': number 
            }
            contacts.append(contact)
            print(f'Contato criado com sucesso!')
    except Exception as err:
        print(f'A criação de contato falhou, tente novamente! \n\nERRO: {err}')

# Exclusão de contato
def remover_contato(contacts, number):
    try:
        for contact in contacts:
            if contact['number'] == number:
                confirm = input(f'[S/N] Confirmar exclusão do contato: {contact['name']} - {contact['number']}? ').strip()
                if confirm == 'S':
                    contacts.remove(contact)
                    print('Contato removido com sucesso!')
                    break
                else:
                    print(f'A remoção foi cancelada.')
            else:
                print(f'A remoção de contato falhou, tente novamente! \n\nERRO: Contato não encontrado.')
    except Exception as err:
        print(f'A remoção de contato falhou, tente novamente! \n\nERRO: {err}')

# Busca um contato
def buscar_contato(contacts, number):
    find = False
    try:
        for i, contact in enumerate(contacts):
            if contact['number'] == number:
                print(f'Contato com o nome {contact['name']} e número {contact['number']} está na posição: {i}!')
                find = True
        if not find:
            print(f'Falha na busca de contato! \n\nERRO: Contato não encontrado.')
    except Exception as err:
        print(f'Falha na busca de contato! \n\nERRO: {err}')

# Mostra todos os contatos
def mostra_contatos(contacts):
    if len(contacts) == 0:
        print(f'Sua lista de contatos está vazia!\n')
    else:
        print(f'----------------------')
        for contact in contacts:
            print(f'Contato: {contact['name']} \nNúmero: {contact['number']}')
        print(f'----------------------')
        
# executo a main depois de carregar todo o código-fonte
if __name__ == "__main__":
    main()