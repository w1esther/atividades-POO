class Comodo:

    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

class Casa:

    def __init__(self):
        self.comodos_casa = []

    def adicionar_comodo(self, nome, tamanho):
        comodo = Comodo(nome, tamanho)
        self.comodos_casa.append(comodo)

    def listar_comodos(self):
        for comodo in self.comodos_casa:
            print(f'Nome: {comodo.nome}, Tamanh0: {comodo.tamanho}')

casa1 = Casa()
casa1.adicionar_comodo('Sala', 20)
casa1.adicionar_comodo('Quarto', 15)
casa1.adicionar_comodo('Cozinha', 10)
casa1.listar_comodos()