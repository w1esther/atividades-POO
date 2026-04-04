class Motor:

    def __init__(self, potencia):
        
        self.potencia = int(potencia)

    def ligar(self):

        print(f'Motor de {self.potencia} cavalos ligado.')

class Carro:

    def __init__(self, modelo, motor):
        
        self.modelo = modelo
        self.motor = motor

    def ligar_carro(self):

        print(f'ligando o {self.modelo}')
        self.motor.ligar()

motor1 = Motor(200)
carro1 = Carro('Onix', motor1)
carro1.ligar_carro()