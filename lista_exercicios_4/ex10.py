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
        if not self.turma_alunos:
            print(" - Nenhum aluno")
        else:
            for aluno in self.turma_alunos:
                print(f" - {aluno.nome_aluno}")

class Escola:

    def __init__(self, nome):
        self.nome_escola = nome
        self.lista_turmas = []

    def criar_turma(self, nome):
        turma = Turma(nome)
        self.lista_turmas.append(turma)
        return turma

    def listar_turmas(self):
        print(f"Escola: {self.nome_escola}")
        for turma in self.lista_turmas:
            print(f"Turma: {turma.nome_turma}")
            turma.exibir_alunos()

aluno1 = Aluno("Maria")
aluno2 = Aluno("João")
aluno3 = Aluno("Ana")
aluno4 = Aluno("Carlos")

escola = Escola("IFRN")

turma1 = escola.criar_turma("1º Ano A")
turma2 = escola.criar_turma("2º Ano B")

turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)

turma2.adicionar_aluno(aluno3)
turma2.adicionar_aluno(aluno4)

escola.listar_turmas()