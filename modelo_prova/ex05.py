class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    # @saldo.setter
    # def saldo(self, saldo):
    #     self.__saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            print('Não é possível depositar valores negativos')
        else:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Valor indisponível para saque!')
        else:
            self.__saldo -= valor

conta1 = Conta('Maria', 2000)
# conta1.saldo = 3000
conta1.depositar(500)
conta1.sacar(1000)
print(conta1.saldo)