class ContaBancaria:


    def __init__(self, nome):
        self.nome_titular = nome
        self.__saldo = 0


    @property
    def saldo(self):
        return self.__saldo


    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo.")
        else:
            self.__saldo = valor


    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return False
        else:
            self.__saldo += valor
            return self.__saldo


    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
            return False
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
            return False
        else:
            self.__saldo -= valor
            return self.__saldo




conta1 = ContaBancaria('Maria')


conta1.depositar(500)
conta1.sacar(200)


print('Saldo atual:', conta1.saldo)


conta1.saldo = 1000
print('Novo saldo:', conta1.saldo)
