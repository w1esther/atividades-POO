from abc import abstractmethod, ABC

class PessoaSistema(ABC):
    @abstractmethod
    def get_identificacao(self):
        pass

class Cliente(PessoaSistema):
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.__idade = None
        self.idade = idade

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            print('Erro: a idade não pode ser negativa!')
        else: 
            self.__idade = idade

    def exibir_dados(self):
        return f'Nome: {self.nome}\nE-mail: {self.email}\nIdade: {self.idade}\n-----------------------------'
    
    def get_identificacao(self):
        return f'IDENTIFICAÇÃO DO CLIENTE POR E-MAIL: {self.email}\n-----------------------------'
    
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.__preco = None
        self.preco = preco

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        if preco < 0:
            print('Erro: o preço não pode ser negativo!')
        else:
            self.__preco = preco

    def __str__(self):
        return f'Código: {self.codigo}\nNome: {self.nome}\nPreço: {self.__preco}\n-----------------------------'
    
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_produtos = []
        self.total = 0

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)

    def calcular_valor_total(self):
        for produto in self.lista_produtos:
            self.total += produto._Produto__preco
        print(f'Total: {self.total}\n-----------------------------')

class ClienteNaoEncontradoError(Exception):
    pass

class Loja:
    def __init__(self):
        self.dicionario_clientes = {}
        self.lista_produtos = []
        self.lista_pedidos = []

    def adicionar_cliente(self, cliente):
        self.dicionario_clientes[cliente.email] = cliente

    def adicionar_produtos(self, produto):
        self.lista_produtos.append(produto)

    def realizar_pedido(self, pedido):
        self.lista_pedidos.append(pedido)

    def buscar_cliente_por_email(self, email):
        if email in self.dicionario_clientes:
            return self.dicionario_clientes[email]
        else:
            raise ClienteNaoEncontradoError(
                'Cliente não encontrado!'
            )

c1 = Cliente('Maria', 'jjfniec@gmail.com', 16)
c1.idade = 17
print(c1.exibir_dados())
print(c1.get_identificacao())
c2 = Cliente('Esther', 'Esther@gmail.com', 16)

produto1 = Produto(39399382, 'Geladeira', 10000)
print(produto1)
produto2 = Produto(83383882, 'Fogão', 5000)
produto3 = Produto(77473883, 'Micro-ondas', 3000)

pedido1 = Pedido(c1)
pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)
pedido1.adicionar_produto(produto3)
pedido1.calcular_valor_total()

loja = Loja()
loja.adicionar_produtos(produto1)
loja.adicionar_produtos(produto2)
loja.adicionar_produtos(produto3)

loja.adicionar_cliente(c1)
loja.adicionar_cliente(c2)
print(loja.buscar_cliente_por_email('Esther@gmail.com'))