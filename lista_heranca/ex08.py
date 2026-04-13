class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        print(f"Motor a combustão de {self.potencia}cv ligado")


class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor  # composição

    def ligar_carro(self):
        print(f"Carro {self.modelo} ligando...")
        self.motor.ligar()


class MotorEletrico(Motor):
    def ligar(self):
        print(f"Motor elétrico de {self.potencia}cv ligado (silencioso)")


class CarroEletrico(Carro):
    def __init__(self, modelo, potencia):
        motor_eletrico = MotorEletrico(potencia)
        super().__init__(modelo, motor_eletrico)

motor1 = Motor(150)
carro1 = Carro("Onix", motor1)
carro2 = CarroEletrico("Tesla", 300)

carro1.ligar_carro()
print("---------------")
carro2.ligar_carro()