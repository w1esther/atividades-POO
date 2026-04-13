class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def exibir_dados(self):
        print(f'Nome: {self.nome}\nSalário: {self.salario}')

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = float(bonus)

    def exibir_dados(self):
        super().exibir_dados()
        print(f'Bonus: {self.bonus}')
        print('-------------------------------')
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_dados(self):
        super().exibir_dados() 
        print(f'Linguagem: {self.linguagem}')
        print('---------------------------')
    
g1 = Gerente('Maria', 4000, 1000)
d1 = Desenvolvedor('Esther', 3500, 'Python')
g1.exibir_dados()
d1.exibir_dados()