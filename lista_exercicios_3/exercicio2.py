class ContaBancaria:

    def __init__(self, nome, saldo):
        
        self.nome_titular = nome 
        self.__saldo = saldo

    @property
    def saldo(self):

        return self.__saldo