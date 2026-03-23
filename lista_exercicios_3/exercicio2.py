class ContaBancaria:

    def __init__(self, nome):
        
        self.nome_titular = nome 
        self.__saldo = 0

    @property
    def saldo(self):

        return self.__saldo

    def depositar(self, valor):

        if valor <= 0:

            return False
        
        else: 

            self.__saldo += valor
            return self.__saldo
    
    def sacar(self, valor):

        if valor > self.__saldo:

            return False
        
        else:

            self.__saldo -= valor
            return self.__saldo
        
    def consultar_saldo(self):

        return self.__saldo
    
conta1 = ContaBancaria('Maria')
conta1.depositar(500)
conta1.sacar(300)
conta1.depositar(-200)
print('Saldo atual:', conta1.consultar_saldo())