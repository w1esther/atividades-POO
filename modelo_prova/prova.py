from abc import ABC, abstractmethod

class DocumentoSaude(ABC):
    @abstractmethod
    def gerar_relatorio(self):
        pass

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Medico(Pessoa):
    def __init__(self, nome, especialidade, crm, endereco):
        super().__init__(nome, endereco)
        self.nome = nome
        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f'Nome: {self.nome}\nEspecialidade: {self.especialidade}\nCRM: {self.crm}\nEndereço: {self.endereco}\n---------------------------------------'
    
class MedicoEspecialista(Medico):
    def __init__(self, nome, especialidade, crm, endereco, registro_especialidade):
        super().__init__(nome, especialidade, crm, endereco)
        self.registro_especialidade = registro_especialidade

    def apresentar_medico(self):
        return f'Nome: {self.nome}\nEspecialidade: {self.especialidade}\nCRM: {self.crm}\nEndereço: {self.endereco}\nRegistro Especialidade: {self.registro_especialidade}\n---------------------------------------'
    

class Paciente(Pessoa):
    def __init__(self, nome, cpf, contato, data_nascimento, endereco):
        super().__init__(nome, endereco)
        self.__cpf = None
        self.cpf = cpf
        self.contato = contato
        # adicionando o atributo data de nascimeto pela inconsistência no enunciado da letra b da 1
        self.data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 11:
            print('Erro: o CPF deve conter exatamente 11 dígitos!')
        else:
            self.__cpf = cpf

    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\n--------------------------------------'

    def exibir_informacoes(self):
        return f'Nome: {self.nome}\nCPF: {self.__cpf}\nContato: {self.contato}\nData de nascimento: {self.data_nascimento}\nEndereço: {self.endereco}\n---------------------------------------'
    
class PacienteNaoCadastradoError(Exception):
    pass

class Clinica:
    def __init__(self, nome_unidade):
        self.nome_unidade = nome_unidade
        self.__corpo_clinico = []
        self.__lista_pacientes = []

    def adicionar_medico(self, medico):
        self.__corpo_clinico.append(medico)

    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    def buscar_paciente_por_cpf(self, cpf):

        for paciente in self.__lista_pacientes:

            if paciente.cpf == cpf:
                return paciente

        raise PacienteNaoCadastradoError(
            'Paciente não cadastrado!'
        )

class Agendamento(DocumentoSaude):
    def __init__(self, medico, paciente, data_hora):
        self.medico = medico
        self.paciente = paciente
        self.data_hora = str(data_hora)

    def gerar_relatorio(self):
        return f'Medico: {self.medico.nome}\nPaciente: {self.paciente.nome}\nDia e Hora: {self.data_hora}\n---------------------------------------'

# a relação entre Agendamento e os objetos medicos/pacientes é de agregação porque esses objetos são agregados à classe assim que é instanciada, pois são passados como parâmetros já no método construtor.
    
medico1 = Medico('Arthur', 'Cirugiao', 3868734, 'Natal')
medico2 = Medico('Maria', 'Pediatria', 838832, 'Natal')
medico_especialista1 = MedicoEspecialista('Vanessa', 'Oftalmo', 388383, 'Natal', 'Oftalmo')
medico_especialista2 = MedicoEspecialista('Pedro', 'Endocrino', 3983383, 'Natal', 'Endocrino')

lista_medico = [medico1, medico2, medico_especialista1, medico_especialista2]

for medico in lista_medico:
    print(medico.apresentar_medico())


paciente1 = Paciente('Vitoria', '72635433214', 98987666, '12/04/2007', 'Natal')
print(paciente1)
print(paciente1.exibir_informacoes())

clinica1 = Clinica('Medfisio')
clinica1.adicionar_medico(medico1)
clinica1.adicionar_paciente(paciente1)
print(clinica1.buscar_paciente_por_cpf('72635433214'))

agendamento1 = Agendamento(medico1, paciente1, '12/07/2025 13:00')
print(agendamento1.gerar_relatorio())

try:
    print(clinica1.buscar_paciente_por_cpf('72635433214'))

except PacienteNaoCadastradoError as erro:
    print(erro)