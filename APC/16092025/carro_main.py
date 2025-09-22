import classes

# Declarando os parametros com keyword + valor para poder declarar em qualquer ordem
meu_carro = classes.Carro(
    marca='Toyota',
    modelo='Yaris', 
    ano=2023, 
    cor='Cinza Prata'
)

carro_vizinho = classes.Carro(
    marca='Chevrolet',
    modelo='Onix', 
    ano=2023, 
    cor='Preto'
)

meu_carro.acelerar(50)
meu_carro.acelerar(30)
meu_carro.frear(20)

carro_vizinho.acelerar(70)

meu_carro.exibir_informacoes()
carro_vizinho.exibir_informacoes()

# usando IS pra ver se é o mesmo objeto
print(f'\nmeu_carro é o mesmo objeto que o carro_vizinho? {meu_carro is carro_vizinho}')

# Verificando se os carros são da mesma classe
print(f'meu_carro é uma instância da classe Carro? {isinstance(meu_carro, classes.Carro)}')
print(f'carro_vizinho é uma instância da classe Carro? {isinstance(carro_vizinho, classes.Carro)}')