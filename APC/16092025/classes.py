class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def dormir(self):
        print(f'{self.nome} {self.sobrenome} está dormindo')

    def andar(self):
        print(f'{self.nome} {self.sobrenome} está andando')

    def comer(self):
        print(f'{self.nome} {self.sobrenome} está comendo')

    def falar(self):
        print(f'{self.nome} {self.sobrenome} está falando')

    def trabalhar(self):
        print(f'{self.nome} {self.sobrenome} está trabalhando')

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        print(f"Objeto Carro da marca {marca} criado!")
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_atual = 0

    def acelerar(self, incremento):
        self.velocidade_atual += incremento
        print(f"O {self.marca} {self.modelo} acelerou para {self.velocidade_atual} km/h.")

    def frear(self, decremento):
        if self.velocidade_atual - decremento >= 0:
            self.velocidade_atual -= decremento
        else:
            self.velocidade_atual = 0
        print(f"O {self.marca} {self.modelo} freou para {self.velocidade_atual} km/h.")
    
    def exibir_informacoes(self):
        print(f"--- Informações do Carro ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade Atual: {self.velocidade_atual} km/h")