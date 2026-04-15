class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

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

class Membro(Pessoa):
    def __init__(self, nome, endereco, id_membro, contato, data_cadastro):
        super().__init__(nome, endereco)
        self.__id_membro = None
        self.id_membro = id_membro
        self.contato = contato
        self.data_cadastro = data_cadastro

    @property
    def id_membro(self):
        return self.__id_membro
    
    @id_membro.setter
    def id_membro(self, id):
        if id < 0:
            print('O ID do membro não pode ser negativo!')
        else:
            self.__id_membro = id

    def __str__(self):
        return f'Nome: {self.nome}, ID: {self.id_membro}'

# b) o método __init__ é o método construtor, podemos entender como a base da nossa classe, já que quando a instanciamos automaticamente o método contrutor é chamado, o parâmetro self serve como uma referenciação à instância atual da classe

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogos_livros = []
        self.lista_membros = []

    def adicionar_livro(self, livro):
        self.catalogos_livros.append(livro)

    def adicionar_membro(self, membro):
        self.lista_membros.append(membro)

class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao):
        self.livro = livro
        self.membro = membro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

# é uma agregação pois eu vou estar usando como atributo objetos ja criados das classes livro e membro, agregando então essas classes

livro1 = Livro("Dom Casmurro", "Machado de Assis", '123456')
livro2 = LivroDigital("1984", "George Orwell","389393", "PDF", 2.5)
livro3 = LivroDigital("O Hobbit", "J.R.R. Tolkien","938844", "EPUB", 3.2)

lista_livros = [livro1, livro2, livro3]

for livro in lista_livros:
    print(livro.exibir_detalhes())
    print(30 * '-')

# Criando membro
membro1 = Membro("Maria", "Rua A", 10, "9999-9999", "15/04/2026")
print("\n=== MEMBRO ===")
print(membro1)

# Testando validação
print("\nTentando colocar ID inválido:")
membro1.id_membro = -5
print(membro1)

# Criando biblioteca
biblioteca = Biblioteca("Biblioteca Central")
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_membro(membro1)

print("\n=== BIBLIOTECA ===")
print(f"Nome: {biblioteca.nome}")
print(f"Quantidade de livros: {len(biblioteca.catalogos_livros)}")
print(f"Quantidade de membros: {len(biblioteca.lista_membros)}")

# Criando empréstimo (agregação)
emprestimo1 = Emprestimo(livro1, membro1, "10/04/2026", "20/04/2026")

print("\n=== EMPRÉSTIMO ===")
print(f"Livro: {emprestimo1.livro.titulo}")
print(f"Membro: {emprestimo1.membro.nome}")
