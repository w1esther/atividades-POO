class Professor:

    def __init__(self, nome, titulacao):
        self.nome = nome
        self.titulacao = titulacao

class Disciplina:

    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

    def mostrar_disciplina(self):
        return f'A disciplina de {self.nome} é ministrada pelo(a) professor(a) {self.professor.nome} {self.professor.titulacao}'
    
p1 = Professor('Joana', 'Mestre')
d1 = Disciplina('Física', p1)
print(d1.mostrar_disciplina())