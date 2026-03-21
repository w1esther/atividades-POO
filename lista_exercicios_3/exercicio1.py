class Estudante:

    def __init__(self, id, nome):
        
        self.__id = int(id)
        self.nome = nome 
        self.__creditos = int(1)

    @property
    def id(self):

        return self.__id
    
    @property
    def creditos(self):

        return self.__creditos
    
    @creditos.setter
    def creditos(self, valor):

        if valor<=0:
            self.__creditos = 1
        else:
            self.__creditos = valor

    def detalhar(self):

        return f'O id {self.id} pertence ao estudante {self.nome} que tem {self.__creditos} de credito'    

estudante1 = Estudante(1, 'Esther')
estudante1.creditos = 14
print(estudante1.detalhar())

estudante2 = Estudante(2, 'Antony')
estudante2.creditos = 30
print(estudante2.detalhar())