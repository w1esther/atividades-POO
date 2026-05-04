from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Membro(Pessoa):
    def __init__(self, nome, endereco, id, data_cadastro):
        super().__init__(nome, endereco)
        self.__id_membro = id
        self.data_cadastro = data_cadastro

    @property
    def id_membro(self):
        return self.__id_membro
    
    @id_membro.setter
    def id_membro(self, id):
        if id < 0:
            print('Não é possível ter ID negativo!')
        else:
            self.__id_membro = id

    def __str__(self):
        return f'Nome: {self.nome}\nID: {self.id_membro}'
    
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def exibir_detalhes(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}'

class LivroDigital(Livro):
    def __init__(self, titulo, autor, isbn, formato, tamanho_mb):
        super().__init__(titulo, autor, isbn)
        self.formato = formato
        self.tamanho_mb = tamanho_mb

    def exibir_detalhes(self):
        return f'Titulo: {self.titulo}\nAutor: {self.autor}\nISBN: {self.isbn}\nFormato: {self.formato}\nTamanho(MB): {self.tamanho_mb}'
    
class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.lista_livros = []
        self.lista_membros = []

    def adicionar_livro(self, titulo, autor, isbn, formato=None, tamanho=None):
        livro = LivroDigital(titulo, autor, isbn, formato, tamanho)
        self.lista_livros.append(livro)

    def adicionar_membro(self, nome, endereco, id, data_cadastro):
        membro = Membro(nome, endereco, id, data_cadastro)
        self.lista_membros.append(membro)

    def listar_livros(self):
        for livro in self.lista_livros:
            print(f'Titulo: {livro.titulo}\nAutor: {livro.autor}\nISBN: {livro.isbn}\nFormato: {livro.formato}\nTamanho: {livro.tamanho_mb}')
            print(30*'-')

    def listar_membros(self):
        for membro in self.lista_membros:
            print(f'Nome: {membro.nome}\nEndereco: {membro.endereco}\nID: {membro.id_membro}\nData cadastro: {membro.data_cadastro}')
            print(30*'-')

    def buscar_livro(self, titulo):
        for livro in self.lista_livros:
            if livro.titulo == titulo:
                print(f'Titulo: {livro.titulo}\nAutor: {livro.autor}\nISBN: {livro.isbn}')

class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao, biblioteca=None):
        self.livro = livro
        self.membro = membro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.biblioteca = biblioteca

    def realizar_emprestimo(self):
        if self.livro not in self.biblioteca.lista_livros:
            print('Livro indisponível no catalogo')
        else:
            print('Emprestimo realizado com sucesso!')

l1 = Livro('O mito da Caverna', 'Platão', 345663)
l2 = LivroDigital('Cosmos', 'Carl Sagan', 3884843, 'PDF', 45)
l3 = LivroDigital('O pequeno Príncipe', 'Antoine de Saint-Exupery', 4885832, 'PDF', 30)

lista_livros = [l1, l2, l3]

for livro in lista_livros:
    print(livro.exibir_detalhes())
    print(30*'-')

b1 = Biblioteca('Leitura')
b1.adicionar_livro('O mito da Caverna', 'Platão', 345663)
b1.adicionar_livro('Cosmos', 'Carl Sagan', 3884843, 'PDF', 45)
b1.adicionar_livro('O pequeno Príncipe', 'Antoine de Saint-Exupery', 4885832, 'PDF', 30)
b1.adicionar_membro('Maria', 'CM', '1','16/04/2026')
b1.adicionar_membro('Pedro', 'CM', '2','16/04/2026')
b1.listar_livros()
b1.listar_membros()
b1.buscar_livro('Cosmos')
membro1 = Membro('Esther', 'CM', 3, '16/04/2026')
emprestimo1 = Emprestimo(l2, membro1, '16/04/2026', '16/05/2026', b1)
emprestimo1.realizar_emprestimo()

# a) Emprestimo é agregação pois usa objetos ja instanciados como atributis
#b) Biblioteca é composição pois cria objetos do tipo Livro e Membro dentro dela