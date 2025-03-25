candidatos = [];

while True:
    decider = int(input("1 - Listar candidadtos\n2 - Adicionar candidato\n3 - Sair\n"));
    if decider == 1:
        if len(candidatos) == 0:
            print("Nenhum candidato cadastrado.");
            continue
        for candidato in candidatos:
            media = (candidato['pt'] + candidato['mt'] + candidato['cg']) / 3;
            notabaixa = True; # (candidato['pt'], candidato['mt'], candidato['cg']) > 5;

            if media >= 7 and notabaixa:
                print(f"Nome: {candidato['nome']}\nMédia: {media:.2f}\nAprovado\n");
            else:
                print(f"Nome: {candidato['nome']}\nMédia: {media:.2f}\nReprovado\n");
    elif decider == 2:
        nome = input("Digite o nome do candidato: ");
        pt = int(input("Digite a nota de Português: "));
        mt = int(input("Digite a nota de Matemática: "));
        cg = int(input("Digite a nota de Conhecimentos Gerais: ")); 

        candidatos.append({
            "nome": nome,
            "pt": pt,
            "mt": mt,
            "cg": cg
        });
    elif decider == 3:
        break;
    else:
        print("Opção inválida.");


