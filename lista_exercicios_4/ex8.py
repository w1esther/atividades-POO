class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:

    def __init__(self, nome):
        self.nome = nome
        self.lista_livros = []

    def adicionar_livro(self, livro):
        self.lista_livros.append(livro)

    def listar_livros(self):
        for livro in self.lista_livros:
            print(f'Título: {livro.titulo}, Autor: {livro.autor}')

livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
livro3 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling")

biblioteca = Biblioteca("Biblioteca Central")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()