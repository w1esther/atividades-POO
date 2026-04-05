class Aluno:

    def __init__(self, nome):
        self.nome_aluno = nome

class Turma:

    def __init__(self, nome):
        self.nome_turma = nome
        self.turma_alunos = []

    def adicionar_aluno(self, aluno):
        self.turma_alunos.append(aluno)

    def exibir_alunos(self):
        for aluno in self.turma_alunos:
            print(aluno.nome_aluno)

class Escola:

    def __init__(self, nome):
        self.nome_escola = nome
        self.lista_turmas = []

    def adicionar_turma(self, turma):
        self.lista_turmas.append(turma)

    def listar_turmas(self):
        for turma in self.lista_turmas:
            print(f'Turma: {turma.nome_turma}')
            for aluno in turma.turma_alunos:
                print(f" - {aluno.nome_aluno}")

aluno1 = Aluno("Maria")
aluno2 = Aluno("João")
aluno3 = Aluno("Ana")
aluno4 = Aluno("Carlos")

turma1 = Turma("1º Ano A")
turma2 = Turma("2º Ano B")

turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)

turma2.adicionar_aluno(aluno3)
turma2.adicionar_aluno(aluno4)

escola = Escola("Escola Estadual")

escola.adicionar_turma(turma1)
escola.adicionar_turma(turma2)

escola.listar_turmas()