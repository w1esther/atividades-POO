class Medico:
    def __init__(self, nome, especialidade, crm):
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f'Nome: {self.nome}\nEspecialidade: {self.especialidade}\nCRM: {self.crm}\n-----------------------------------'

class Paciente:
    def __init__(self, nome, cpf, contato):
        self.nome = nome
        self.cpf = cpf
        self.contato = contato

    def exibir_dados(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}'