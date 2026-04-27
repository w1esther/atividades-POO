from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):

    @abstractmethod
    def ligar(self):
        return 'Ligando...'
    
    @abstractmethod
    def desligar(self):
        return 'Desligando...'

class Carregavel(ABC):

    @abstractmethod
    def carregar(self):
        return 'Carregando...'

class Smartphone(DispositivoEletronico, Carregavel):
    def ligar(self):
        return 'Smartphone Ligando...'
    
    def desligar(self):
        return 'Smartphone Desligando...'
    
    def carregar(self):
        return 'Smartphone carregando'

class Notebook(DispositivoEletronico, Carregavel):

    def ligar(self):
        return 'Notebook Ligando...'
    
    def desligar(self):
        return 'Notebook Desligando...'
    
    def carregar(self):
        return 'Notebook Carregando...'

class FoneDeOuvido(DispositivoEletronico):

    def ligar(self):
        return 'Fone de Ouvido Ligando...'
    
    def desligar(self):
        return 'Fone de Ouvido Desligando...'
    
s1 = Smartphone()
n1 = Notebook()
f1 = FoneDeOuvido()

lista_dispositivos_eletronicos = [s1, n1, f1]
lista_carregaveis = [s1, n1]

for disipotivo in lista_dispositivos_eletronicos:
    print(disipotivo.ligar(),'\n',disipotivo.desligar())

for dispositivo in lista_carregaveis:
    print(dispositivo.carregar())