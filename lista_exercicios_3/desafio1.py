
class Produto:


    def __init__(self, nome, preco, qnt_incial):


        self.__nome = nome
        self.__preco = float(preco)
        self.__quantidade_em_estoque = qnt_incial


    def vender(self, quantidade):


        if quantidade > self.__quantidade_em_estoque:


            return False
       
        else:


            self.__quantidade_em_estoque -= quantidade
            return self.__quantidade_em_estoque
       
    def repor_estoque(self, quantidade):


        if quantidade <= 0:


            return False
       
        else:


            self.__quantidade_em_estoque += quantidade
            return self.__quantidade_em_estoque
       
    def get_nome(self):


        return self.__nome
   
    @property
    def preco(self):


        return self.__preco
   
    @preco.setter


    def preco(self, novo_preco):


        if novo_preco <= 0:


            return False
       
        else:


            self.__preco = novo_preco
            return self.__preco
       
    @property
    def quantidade_em_estoque(self):


        return self.__quantidade_em_estoque
   
    @quantidade_em_estoque.setter


    def quantidade_em_estoque(self, quantidade):


        if quantidade < 0:


            return False
       
        else:


            self.__quantidade_em_estoque += quantidade
            return self.__quantidade_em_estoque
   
    def get_quantidade_em_estoque(self):


        return self.__quantidade_em_estoque
   
    def get_preco(self):


        return self.__preco
   
produto1 = Produto('notebook', 3500.00, 10)


produto1.preco = 4000.00
print(f"Produto: {produto1.get_nome()}, Preço: R${produto1.get_preco():.2f}, Estoque: {produto1.get_quantidade_em_estoque()}")


produto1.vender(3)
produto1.repor_estoque(5)
produto1.vender(15)


produto1.quantidade_em_estoque = 30


print(f"Estoque atual: {produto1.get_quantidade_em_estoque()}")