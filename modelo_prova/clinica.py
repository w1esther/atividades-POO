from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class PessoaClinica(ABC):

    @abstractmethod
    def get_identificacao(self):
        pass

class Paciente(Pessoa):
    def __init__(self, nome, telefone, cpf, idade):
        super().__init__(nome, telefone)
        self.cpf = cpf
        self.__idade = None
        self.idade = idade

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade<0:
            print('Erro: a idade não pode ser negativa!')
        else:
            self.__idade = idade

    def exibir_dados(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'
    
    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'
    
    
class Medico(PessoaClinica):
    def __init__(self, nome, crm, especialidade):
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade

    def __str__(self):
        return f'Nome: {self.nome}\nCRM: {self.crm}\nEspecialidade: {self.especialidade}'
    
    def get_identificacao(self):
        return self.crm

class Clinica:
    def __init__(self, nome):
        self.nome = nome
        self.lista_pacientes = []
        self.lista_medicos = []
    
    def adicionar_pacientes(self, paciente):
        self.lista_pacientes.append(paciente)

    def adicionar_medico(self, medico):
        self.lista_medicos.append(medico)

    def buscar_paciente_por_cpf(self, cpf):
        for paciente in self.lista_pacientes:
            if paciente.cpf == cpf:
                return paciente

        raise PacienteNaoEncontradoError('Erro: paciente não encontrado')

class Consulta:
    def __init__(self, paciente, medico, data_consulta, horario_consulta):
        self.paciente = paciente
        self.medico = medico
        self.data_consulta = data_consulta
        self.horario_consulta = horario_consulta

    def exibir_dados(self):
        return f'Paciente: {self.paciente}\nMedico: {self.medico}\nData: {self.data_consulta}\nHorário: {self.horario_consulta}'

class ConsultaOnline(Consulta):
    def __init__(self, paciente, medico, data_consulta, horario_consulta):
        super().__init__(paciente, medico, data_consulta, horario_consulta)

    def exibir_dados(self):
        return f'Paciente: {self.paciente}\nMedico: {self.medico}\nData: {self.data_consulta}\nHorário: {self.horario_consulta}'
    
    
p1 = Paciente('Joao', 88292982, 288832, 28)
p2 = Paciente('Maria', 99393993, 929393829, 29)
m1 = Medico('Maria', 2929822, 'Clinico Geral')
m2 = Medico('Joao', 8288383992, 'Endrocnologista')
c1 = Consulta(p1, m1, '17/03/2025', '13:00')
c1online = ConsultaOnline(p2, m2, '23/08/2025', '10:00')

lista_consultas = [c1, c1online]

for consulta in lista_consultas:
    print(consulta.exibir_dados())