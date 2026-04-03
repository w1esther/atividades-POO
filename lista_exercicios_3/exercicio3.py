class ContaBancaria:


    def __init__(self, nome):
        self.nome_titular = nome
        self.__saldo = 0


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


    def get_saldo(self):
        return self.__saldo


    def set_saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo.")
            return False
        else:
            self.__saldo = valor
            return self.__saldo

conta1 = ContaBancaria('Maria')

conta1.depositar(500)
conta1.sacar(200)

print('Saldo atual:', conta1.get_saldo())

conta1.set_saldo(1000)
print('Novo saldo:', conta1.get_saldo())
