class ContaCorrente:

    def __init__(self, nome, cpf, saldo): 
         
        self.nome_correntista = nome
        self.cpf_correntista = int(cpf)
        self.saldo_correntista = int(saldo)

    def depositar(self, valor_deposito):

        novo_salado = self.saldo_correntista + valor_deposito
        self.saldo_correntista = novo_salado

        return self.saldo_correntista
    
    def sacar(self, valor_saque):

        novo_saldo = self.saldo_correntista - valor_saque
        self.saldo_correntista = novo_saldo

        return self.saldo_correntista
    
    def mostrar_saldo(self):

        return f'O correntista {self.nome_correntista} de CPF {self.cpf_correntista} tem saldo atual de {self.saldo_correntista} reais'
    
correntista1 = ContaCorrente('Maria', 12346578910, 1000)
correntista1.sacar(100)
correntista1.depositar(200)
print(correntista1.mostrar_saldo())