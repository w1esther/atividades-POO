from abc import ABC, abstractmethod


# =========================================
# QUESTÃO 4A — HERANÇA
# =========================================

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco


# =========================================
# QUESTÃO 5A — CLASSE ABSTRATA
# =========================================

class DocumentoSaude(ABC):

    @abstractmethod
    def gerar_relatorio(self):
        pass


# =========================================
# QUESTÃO 1 + QUESTÃO 3
# =========================================

class Paciente(Pessoa):

    def __init__(self, nome, endereco, cpf, contato):
        super().__init__(nome, endereco)

        self.__cpf = None
        self.cpf = cpf

        self.contato = contato

    # QUESTÃO 3A — PROPERTY
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):

        cpf = str(cpf)

        if len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf

        else:
            print('Erro: CPF inválido!')

    # QUESTÃO 1C
    def exibir_informacoes(self):
        return f'''
Nome: {self.nome}
CPF: {self.cpf}
Contato: {self.contato}
Endereço: {self.endereco}
-----------------------------
'''

    # QUESTÃO 3B
    def __str__(self):
        return f'Paciente: {self.nome} | CPF: {self.cpf}'


# =========================================
# QUESTÃO 1A e 1B
# =========================================

class Medico(Pessoa):

    def __init__(self, nome, endereco, especialidade, crm):
        super().__init__(nome, endereco)

        self.especialidade = especialidade
        self.crm = crm

    def apresentar_medico(self):
        return f'''
Nome: {self.nome}
CRM: {self.crm}
Especialidade: {self.especialidade}
Endereço: {self.endereco}
-----------------------------
'''


# =========================================
# QUESTÃO 4B — POLIMORFISMO
# =========================================

class MedicoEspecialista(Medico):

    def __init__(
        self,
        nome,
        endereco,
        especialidade,
        crm,
        registro_especialidade
    ):

        super().__init__(
            nome,
            endereco,
            especialidade,
            crm
        )

        self.registro_especialidade = registro_especialidade

    # POLIMORFISMO
    def apresentar_medico(self):
        return f'''
Nome: {self.nome}
CRM: {self.crm}
Especialidade: {self.especialidade}
Registro Especialidade: {self.registro_especialidade}
Endereço: {self.endereco}
-----------------------------
'''


# =========================================
# QUESTÃO 2A — COMPOSIÇÃO
# =========================================

class Clinica:

    def __init__(self, nome_unidade):

        self.nome_unidade = nome_unidade

        self.__corpo_clinico = []
        self.__lista_pacientes = []

    def adicionar_medico(self, medico):
        self.__corpo_clinico.append(medico)

    def adicionar_paciente(self, paciente):
        self.__lista_pacientes.append(paciente)

    # QUESTÃO 5B
    def buscar_paciente_por_cpf(self, cpf):

        for paciente in self.__lista_pacientes:

            if paciente.cpf == cpf:
                return paciente

        raise PacienteNaoCadastradoError(
            'Paciente não cadastrado!'
        )


# =========================================
# QUESTÃO 2B + QUESTÃO 5A
# =========================================

class Agendamento(DocumentoSaude):

    def __init__(self, medico, paciente, data_hora):

        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora

    # IMPLEMENTAÇÃO DA CLASSE ABSTRATA
    def gerar_relatorio(self):

        return f'''
========== RELATÓRIO ==========
Paciente: {self.paciente.nome}
Médico: {self.medico.nome}
Especialidade: {self.medico.especialidade}
Horário: {self.data_hora}
===============================
'''


# =========================================
# QUESTÃO 5B — EXCEÇÃO
# =========================================

class PacienteNaoCadastradoError(Exception):
    pass


# =========================================
# PROGRAMA PRINCIPAL
# =========================================

# PACIENTES
p1 = Paciente(
    'Esther',
    'Natal/RN',
    '12345678901',
    '84999999999'
)

p2 = Paciente(
    'Maria',
    'Parnamirim/RN',
    '98765432100',
    '84888888888'
)

print(p1.exibir_informacoes())
print(p2)

# MÉDICOS
m1 = Medico(
    'Carlos',
    'Natal/RN',
    'Clínico Geral',
    'CRM123'
)

m2 = MedicoEspecialista(
    'Fernanda',
    'Natal/RN',
    'Neurologia',
    'CRM456',
    'RQE999'
)

# POLIMORFISMO
lista_medicos = [m1, m2]

for medico in lista_medicos:
    print(medico.apresentar_medico())

# CLÍNICA
clinica = Clinica('MedFisio')

clinica.adicionar_medico(m1)
clinica.adicionar_medico(m2)

clinica.adicionar_paciente(p1)
clinica.adicionar_paciente(p2)

# AGENDAMENTO
consulta1 = Agendamento(
    m2,
    p1,
    '20/05/2026 - 14:00'
)

print(consulta1.gerar_relatorio())

# TRY EXCEPT
try:

    paciente = clinica.buscar_paciente_por_cpf(
        '12345678901'
    )

    print(paciente)

except PacienteNaoCadastradoError as erro:
    print(erro)