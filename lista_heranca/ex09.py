class Motor:
    def __init__(self, potencia, **kwargs):
        super().__init__(**kwargs)
        self.potencia = potencia

    def ligar_motor(self):
        print(f"Motor de {self.potencia}cv ligado")

    def exibir_info(self):
        print(f"Potência: {self.potencia}cv")

class Eletrico:
    def __init__(self, bateria, **kwargs):
        super().__init__(**kwargs)
        self.bateria = bateria

    def carregar(self):
        print(f"Carregando bateria de {self.bateria}kWh")

    def exibir_info(self):
        print(f"Bateria: {self.bateria}kWh")

class Combustao:
    def __init__(self, tanque, **kwargs):
        super().__init__(**kwargs)
        self.tanque = tanque

    def abastecer(self):
        print(f"Abastecendo tanque de {self.tanque}L")

    def exibir_info(self):
        print(f"Tanque: {self.tanque}L")

class CarroEletrico(Motor, Eletrico):
    def __init__(self, potencia, bateria):
        super().__init__(potencia=potencia, bateria=bateria)

    def exibir_info(self):
        print("Carro Elétrico:")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)

class CarroHibrido(Motor, Eletrico, Combustao):
    def __init__(self, potencia, bateria, tanque):
        super().__init__(potencia=potencia, bateria=bateria, tanque=tanque)

    def exibir_info(self):
        print("Carro Híbrido:")
        Motor.exibir_info(self)
        Eletrico.exibir_info(self)
        Combustao.exibir_info(self)

carro1 = CarroEletrico(150, 50)
carro2 = CarroHibrido(200, 40, 60)

carro1.exibir_info()
print("-------------------")
carro2.exibir_info()