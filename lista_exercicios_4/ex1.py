class Cidade:

    def __init__(self, nome):
        
        self.nome = nome

class Pessoa:

    def __init__(self, nome, cidade):
        
        self.nome = nome
        self.cidade = cidade.nome

    def apresentacao_pessoa(self):

        print(f'eu sou {self.nome} e moro na cidade {self.cidade}')

class Animal:

    def __init__(self, nome, dono):
        
        self.nome = nome
        self.dono = dono.nome

    def apresentacao_animal(self):

        print(f'eu sou {self.nome} e meu dono é {self.dono}')

cidade1 = Cidade('Ceará-Mirim')
pessoa1 = Pessoa('Maria', cidade1)
pessoa1.apresentacao_pessoa()
animal1 = Animal('Toto', pessoa1)
animal1.apresentacao_animal()