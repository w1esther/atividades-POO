from abc import ABC, abstractmethod

class PessoaSistema(ABC):

    @abstractmethod
    def get_identificacao(self):
        pass

class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Aluno(Pessoa, PessoaSistema):
    def __init__(self, nome, matricula, idade, telefone):
        super().__init__(nome, telefone)
        self.matricula = matricula
        self.__idade = None
        self.idade = idade

    def get_identificacao(self):
        return f'Matricula: {self.matricula}\n-----------------------------'

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade<0:
            print('Erro: a idade não pode ser negativa')
        else:
            self.__idade = idade

    def exibir_dados(self):

        return f'Nome: {self.nome}\nMatrícula: {self.matricula}\nIdade: {self.idade}\nTelefone: {self.telefone} \n-----------------------------'

class Disciplina:
    def __init__(self, nome_disciplina, carga_horaria, professor):
        self.nome_disciplina = nome_disciplina
        self.carga_horaria = carga_horaria
        self.professor = professor

    def __str__(self):
        return f'Nome {self.nome_disciplina}\nCarga Horária: {self.carga_horaria}\nProfessor: {self.professor}\n-----------------------------'
    
class AlunoBolsista(Aluno):
    def __init__(self, nome, matricula, idade, telefone, percentual_bolsa):
        super().__init__(nome, matricula, idade, telefone)
        self.percentual_bolsa = percentual_bolsa

    def exibir_dados(self):

        return f'Nome: {self.nome}\nMatrícula: {self.matricula}\nIdade: {self.idade}\nTelefone: {self.telefone}\nPercentual Bolsa: {self.percentual_bolsa} \n-----------------------------'

# b) o método __init__ é o método construtor da minha classe, chamado assim que a instancio, criando então um objeto, é como a base.
# o parâmetro self se refere ao própip objeto

class AlunoNaoEncontradoError(Exception):
    pass

class Turma:
    def __init__(self, nome_turma):
        self.nome_turma = nome_turma
        self.dicionario_alunos = {}
        self.lista_disciplinas = []

    def adicionar_aluno(self, aluno):
        self.dicionario_alunos[aluno.matricula] = aluno

    def adicionar_disciplina(self, disciplina):
        self.lista_disciplinas.append(disciplina)

    def buscar_aluno_por_matricula(self, matricula):
        if matricula in self.dicionario_alunos:
            return self.dicionario_alunos[matricula]
        
        raise AlunoNaoEncontradoError(
            'Aluno não encontrado'
        )

class Matricula:
    def __init__(self, aluno, disciplina, data_matricula):
        self.aluno = aluno
        self.disciplina = disciplina
        self.data_matricula = data_matricula

# essa relação é de agregação porque eu uso objetos já instanciados como atributos para compor essa outra classe

aluno1 = Aluno('Esther', 9394839, 16, 4737283)
print(aluno1.get_identificacao())

aluno2 = Aluno('Maria', 754679, 17, 8765456)

aluno_bolsista1 = AlunoBolsista('Joao', 8393832, 15, 8483782, '20%')

disciplina1 = Disciplina('Geometria Analítica', 5, 'Jefferson')
print(disciplina1)

turma1 = Turma('INFO2V')
turma1.adicionar_aluno(aluno1)
turma1.adicionar_aluno(aluno2)
turma1.adicionar_aluno(aluno_bolsista1)
turma1.adicionar_disciplina(disciplina1)

try:
    aluno = turma1.buscar_aluno_por_matricula(9394839)
    print(aluno.exibir_dados())

except AlunoNaoEncontradoError as erro:
    print(erro)

try:
    aluno = turma1.buscar_aluno_por_matricula(93949)
    print(aluno.exibir_dados())

except AlunoNaoEncontradoError as erro:
    print(erro)

matricula1 = Matricula(aluno1, disciplina1, '18/05/2026')

lista_alunos = [aluno1, aluno_bolsista1, aluno2]

for aluno in lista_alunos:
    print(aluno.exibir_dados())