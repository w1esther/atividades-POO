class Processador:

    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.velocidade = velocidade

class Memoria:

    def __init__(self, capacidade):
        self.capacidade = capacidade

class Computador:

    def __init__(self, modelo, velocidade, capacidade):
        self.processador = Processador(modelo, velocidade)
        self.memoria = Memoria(capacidade)

    def exibir_configuracoes(self):

        return f'O computador tem o processador {self.processador.modelo} de velocidade {self.processador.velocidade} e memoria com capacidade de {self.memoria.capacidade}'
    
computador1 = Computador('Intel i5', '3.0GHz', '8GB')
print(computador1.exibir_configuracoes())