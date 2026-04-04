class Autor:

    def __init__(self, nome):
        
        self.nome_autor = nome

class Livro:

    def __init__(self, nome_livro, nome_autor):
        
        self.nome_livro = nome_livro

        self.nome_autor = nome_autor.nome_autor
    
    def apresentacao_livro(self):

        print(f'o Livro {self.nome_livro} pertence ao autor(a) {self.nome_autor}')

autor1 = Autor('Graciliano Ramos')
livro1 = Livro('Vidas Secas', autor1)
livro1.apresentacao_livro()