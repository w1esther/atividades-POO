class Jogador:

    def __init__(self, nome, posicao):
        self.nome_jogador = nome
        self.posicao_jogador = posicao

class Time:

    def __init__(self, nome):
        self.nome_time = nome
        self.lista_jogadores = []

    def adicionar_jogador(self, jogador):
        self.lista_jogadores.append(jogador)

    def listar_jogadores(self):
        for jogador in self.lista_jogadores:
            print(f'-{jogador.nome_jogador}, {jogador.posicao_jogador}')

j1 = Jogador("Neymar", "Atacante")
j2 = Jogador("Casemiro", "Volante")
j3 = Jogador("Alisson", "Goleiro")
time = Time("Brasil")
time.adicionar_jogador(j1)
time.adicionar_jogador(j2)
time.adicionar_jogador(j3)
time.listar_jogadores()