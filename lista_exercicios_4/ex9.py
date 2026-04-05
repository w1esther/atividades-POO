class ItemPedido:

    def __init__(self, produto, quantidade, preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

class Pedido:

    def __init__(self):
        self.lista_itens = []

    def adicionar_item(self, produto, quantidade, preco):
        item = ItemPedido(produto, quantidade, preco)
        self.lista_itens.append(item)

    def calcular_total(self):
        total = 0
        for item in self.lista_itens:
            total += item.quantidade * item.preco
        return total
    
pedido = Pedido()

pedido.adicionar_item("Camiseta", 2, 50)
pedido.adicionar_item("Tênis", 1, 200)
pedido.adicionar_item("Boné", 3, 30)

print("Total do pedido:", pedido.calcular_total())