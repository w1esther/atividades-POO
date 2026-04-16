class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_info(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_info(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nMatricula: {self.matricula}'

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def exibir_info(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nSalario: {self.salario}'

a1 = Aluno('Maria', 15, 3494994)
a2 = Aluno('Paulo', 14, 8929345)
p1 = Professor('Eva', 38, 3500)
p2 = Professor('João', 39, 3500)

lista_alunos_professores = [a1, a2, p1, p2]

for aluno_professor in lista_alunos_professores:
    print(aluno_professor.exibir_info())
    print(30*'-')