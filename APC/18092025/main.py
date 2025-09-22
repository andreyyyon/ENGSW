import classes

nome = input('Digite o nome: ')
idade = input('Digite o idade: ')
email = input('Digite o email: ')
celular = input('Digite o celular: ')

pessoa1 = classes.Pessoa(nome, idade, email, celular)
pessoa1.nome = nome
pessoa1.idade = idade
pessoa1.email = email
pessoa1.celular = celular

pessoa1.exibir_dados()