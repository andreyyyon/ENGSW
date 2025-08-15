# 7 – F.U.P para simular uma agenda com as operações de inclusão, alteração, 
# exclusão, listar e sair. Dados que deverão ser cadastrados: Nome e telefone.
# Validar para que não existe mais de um telefone cadastrado na agenda.
# Validar para que o nome e o telefone são preenchidos pelo usuário antes de 
# adicionar na agenda. Caso o telefone ou agenda não for preenchido deverá ser 
# informado de campo vazio.
# Na exclusão deverá ser solicitado o nr do telefone. Caso não exista na agenda, 
# deverá exibir mensagem para o usuário: Nr telefone não existente.

contacts = []

while True:
    print(f'1 - Incluir contato\n2 - Alterar contato\n3 - Excluir contato\n4 - Listar contatos\n5 - Sair')
    choice = input('Escolha uma opção: ').strip()

    # condição pra sair
    if choice == '5': break

    # inclusão
    if choice == '1':
        try:
            name = input('Digite o nome do contato: ').strip()
            number = input('Digite o número de telefone: ').strip()

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
    elif choice == '2':
        try:
            number = input('Qual contato deseja alterar? ').strip()
            for contact in contacts:
                if contact['number'] == number:
                    new_name = input('Digite o nome do contato: ').strip()
                    new_number = input('Digite o número de telefone: ').strip()

                    if not new_name or not new_number: 
                        print(f'A alteração de contato falhou, tente novamente! \n\n ERRO: Nome e telefone não podem estar vazio.')
                    elif any(x['number'] == new_number and number != new_number for x in contacts):
                        print(f'A alteração de contato falhou, tente novamente! \n\nERRO: Telefone já cadastrado.')   
                    else:
                        contact['name'] = new_name
                        contact['number'] = new_number
                        print('Contato alterado com sucesso!')
                else:
                    print(f'A alteração de contato falhou, tente novamente! \n\nERRO: Contato não encontrado.')
        except Exception as err:
            print(f'A alteração de contato falhou, tente novamente! \n\nERRO: {err}')
    elif choice == '3':
        try:
            number = input('Qual contato deseja excluir? ').strip()
            for contact in contacts:
                if contact['number'] == number:
                    confirm = input(f'[S/N] Confirmar exclusão do contato: {contact['name']} - {contact['number']}? ').strip()
                    if confirm == 'S':
                        contacts.remove(contact)
                        print('Contato removido com sucesso!')
                    else:
                        print(f'A remoção foi cancelada.')
                else:
                    print(f'A remoção de contato falhou, tente novamente! \n\nERRO: Contato não encontrado.')
        except Exception as err:
            print(f'A remoção de contato falhou, tente novamente! \n\nERRO: {err}')
    elif choice == '4':
        if len(contacts) == 0:
            print(f'Sua lista de contatos está vazia!\n')
        else:
            for contact in contacts:
                print(f'Contato: {contact['name']} \nNúmero: {contact['number']}')
    else:
        print('Digite uma opção valida.')