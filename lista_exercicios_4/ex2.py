class Motor:

    def __init__(self, potencia):
        if Carro is None:
            raise ValueError("Motor precisa estar associado a um Carro")
        
        self.potencia = int(potencia)

    def ligar(self):

        print(f'Motor de {self.potencia} cavalos ligado.')

class Carro:

    def __init__(self, modelo, motor):
        
        self.modelo = modelo
        self.motor = Motor(motor)

    def ligar_carro(self):

        print(f'ligando o {self.modelo}')
        self.motor.ligar()

carro1 = Carro('Onix', 200)
carro1.ligar_carro()