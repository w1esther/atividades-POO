class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def exibir_detalhes(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}'

class Membro:
    def __init__(self, nome, id_membro, contato):
        self.nome = nome
        self.id_membro = id_membro
        self.contato = contato

# b) o método __init__ é o método construtor da minha classe, aquele que é chamado assim que eu a instancio, sendo como a base dela.

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo_livros = []
        self.lista_membros = []

    def adicionar_livro(self, livro):
        self.catalogo_livros.append(livro)
    
    def adicionar_membro(self, membro):
        self.lista_membros.append(membro)
    
m1 = Membro('Esther', 1, 288392028)
b1 = Biblioteca('Bibliotec IFRM')
b1.adicionar_membro(m1)
# print(self.lista_membros)    