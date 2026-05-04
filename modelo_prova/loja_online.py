from abc import ABC, abstractmethod

class ProdutoBase(ABC):
    def __init__(self, nome, preco):
        super().__init__()
        self.nome = nome
        self.__preco = None
        self.preco = preco

    @abstractmethod
    def calcular_preco_final(self):
        pass

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            print('O preço não pode ser negativo!')
        else:
            self.__preco = preco

class Vendavel(ABC):
    @abstractmethod
    def calcular_desconto(self):
        pass

class ProdutoFisico(ProdutoBase, Vendavel):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso
        self.frete = peso*2
        self.preco_final = preco + self.frete

    def calcular_preco_final(self):
        self.preco_final =  self.preco + self.frete
        return f'O preço final do(a) {self.nome} é: R$ {self.preco_final}'
    
    def calcular_desconto(self, desconto):
        valor_desconto = desconto/100
        preco_desconto = self.preco_final - (self.preco_final*valor_desconto)
        return f'O valor final com {desconto}% de desconto foi: R$ {preco_desconto}'     

class ProdutoDigital(ProdutoBase, Vendavel):
    def __init__(self, nome, preco, tamanho_mb):
        super().__init__(nome, preco)
        self.tamanho_mb = tamanho_mb
        self.preco_final = preco

    def calcular_preco_final(self):
        self.preco_final =  self.preco
        return f'O preço final do(a) {self.nome} é: R$ {self.preco_final}'
    
    def calcular_desconto(self, desconto):
        valor_desconto = desconto/100
        preco_desconto = self.preco_final - (self.preco_final*valor_desconto)
        return f'O valor final com {desconto}% de desconto foi: R$ {preco_desconto}'  

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Carrinho:
    def __init__(self):
        self.lista_produto = []

    def adicionar_produto(self, produto):
        self.lista_produto.append(produto)
        return 'Produto adicionado com sucesso!'
    
    def calcular_total(self):
        somatorio = 0
        for produto in self.lista_produto:
            somatorio += produto.calcular_preco_final()
        return f'Preço total de R$ {somatorio}'
    
class Pedido():
    def __init__(self, cliente, carrinho):
        self.cliente = cliente 
        self.carrinho = carrinho

    def finalizar_pedido(self):
        return 'Pedido finalizado com sucesso!'
    
pf1 = ProdutoFisico('Lapis', 3, 0.100)
pf2 = ProdutoFisico('Caderno', 75, 0.500)
pd1 = ProdutoDigital('Ebook', 30, 12)
pd2 = ProdutoDigital('Apostila', 100, 32)

lista_produtos = [pf1, pf2, pd1, pd2]

for produto in lista_produtos:
    print(produto.calcular_preco_final())

# a) Porque eu uso objetos de ProdutoDigital e ProdutoFisico agregados a ele na lista de produtos
# b)Porque nela eu crio objetos do tipo Cliente e Carrinho agregados a ele
# c) no momento em que eu intero a lista de produtos chamando o métpdp calcular_preco_final() para cada um deles

# VERSAO_CORRIGIDA

from abc import ABC, abstractmethod

class ProdutoBase(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = None
        self.preco = preco  # usa setter

    @abstractmethod
    def calcular_preco_final(self):
        pass

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            print('O preço não pode ser negativo!')
        else:
            self.__preco = preco

class Vendavel(ABC):
    @abstractmethod
    def calcular_desconto(self):
        pass

class ProdutoFisico(ProdutoBase, Vendavel):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    def calcular_preco_final(self):
        frete = self.peso * 2
        return self.preco + frete

    def calcular_desconto(self):
        return self.calcular_preco_final() * 0.10  # 10%

class ProdutoDigital(ProdutoBase, Vendavel):
    def __init__(self, nome, preco, tamanho_mb):
        super().__init__(nome, preco)
        self.tamanho_mb = tamanho_mb

    def calcular_preco_final(self):
        return self.preco

    def calcular_desconto(self):
        return self.calcular_preco_final() * 0.20  # 20%

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Carrinho:
    def __init__(self):
        self.lista_produto = []

    def adicionar_produto(self, produto):
        self.lista_produto.append(produto)

    def calcular_total(self):
        total = 0
        for produto in self.lista_produto:
            preco = produto.calcular_preco_final()
            desconto = produto.calcular_desconto()
            total += (preco - desconto)
        return total

class Pedido:
    def __init__(self, cliente, carrinho):
        self.cliente = cliente
        self.carrinho = carrinho

    def finalizar_pedido(self):
        total = self.carrinho.calcular_total()
        return f'Pedido de {self.cliente.nome} finalizado! Total: R$ {total:.2f}'

pf1 = ProdutoFisico('Lápis', 3, 0.1)
pf2 = ProdutoFisico('Caderno', 75, 0.5)
pd1 = ProdutoDigital('Ebook', 30, 12)
pd2 = ProdutoDigital('Apostila', 100, 32)

lista_produtos = [pf1, pf2, pd1, pd2]

print("=== POLIMORFISMO ===")
for produto in lista_produtos:
    print(f'{produto.nome}: R$ {produto.calcular_preco_final():.2f}')

carrinho = Carrinho()
for produto in lista_produtos:
    carrinho.adicionar_produto(produto)

cliente = Cliente('Maria', '123456789')
pedido = Pedido(cliente, carrinho)

print("\n=== PEDIDO ===")
print(pedido.finalizar_pedido())