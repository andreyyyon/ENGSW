# Aula sobre dicionários

tabela = {
    'Alface':0.45,
    'Batata':1.20,
    'Tomate':2.30,
    'Feijao':1.50
}

# Printa o dicionario
print(tabela)
# Printa valor da chave em especifico
print(tabela['Alface'])
# Printa as chaves
print(tabela.keys())

# Lista em um dicionario
estoque = {
    'frutas': ['maca', 'banana', 'laranja'],
    'vegetais': ['cenoura', 'batata', 'brocolis']
}
# Printa a lista dentro do dicionario
print(estoque['frutas'])
print(estoque['vegetais'][1])

# Values é o metodo para ter acesso a todos os valores das chaves
print(estoque.values())

# Get é o metodo para ter o acesso do valor de uma chave em especifico
print(estoque.get('frutas'))

# Get com mensagem custom de chave nao existente
print(estoque.get('teste', 'não existe'))

aluno = {
    'nome': 'Andrey',
    'idade': 20,
    'curso': 'Eng. Software'
}

# Exemplo de leitura de dicionario
for chave, valor in aluno.items():
    print(chave, ':', valor)

# Manipulando valores
pessoa = {}
chave = 'nome'
chAltura = 'altura'

pessoa[chave] = 'Joao'
pessoa[chAltura] = 1.80
print(pessoa)