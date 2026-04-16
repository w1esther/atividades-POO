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

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Pedido:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade

    def calcular_total(self):
        total = self.produto.preco * self.quantidade
        return total

produto1 = Produto('Bolo', 150)
c1 = Cliente('Maria', 12345678)
pedido1 = Pedido(c1, produto1, 2)
print(pedido1.calcular_total())

# É uma agregação porque a classe Pedido utiliza objetos das classes Cliente e Produto que são criados fora dela. Esses objetos existem independentemente do Pedido, ou seja, se um Pedido for removido, o Cliente e o Produto continuam existindo.