class Carro:

    def __init__(self, marca, modelo, ano): 

        self.marca = marca
        self.modelo = modelo 
        self.ano = int(ano)

    def exibir_dados(self):

        return f'O carro é do modelo {self.modelo} da marca {self.marca} e do ano de {self.ano}'
    
carro1 = Carro('BYD', 'Dolphin Mini', 2020)
print(carro1.exibir_dados())