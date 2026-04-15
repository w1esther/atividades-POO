class Produto:

    def __init__(self, nome,preco):
        self.nome = nome
        self.__preco = None
        self.preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            print('O preço não pode ser negativo!')
        else:
            self.__preco = preco

produto1 = Produto('Água', 5)
produto1.preco = -7
print(produto1.preco)