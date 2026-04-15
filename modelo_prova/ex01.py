class Filme:

    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def exibir_detalhes(self):

        print(f'Titulo: {self.titulo}\nDiretor: {self.diretor}')

class FilmeSerie(Filme):

    def __init__(self, titulo, diretor, temporadas):
        super().__init__(titulo, diretor)
        self.temporadas = temporadas

    def exibir_detalhes(self):

        print(f'Titulo: {self.titulo}\nDiretor: {self.diretor}\nTemporadas: {self.temporadas}')

fs1 = FilmeSerie('Anne', 'Marcos', 3)
fs2 = FilmeSerie('stranger things', 'Roberta', 5)
f3 = Filme('interestrelar', 'pedro')

lista_filmes_series = [fs1, fs2, f3]

for filme_serie in lista_filmes_series:
    filme_serie.exibir_detalhes()
    print('-' * 30)

fs1.exibir_detalhes()