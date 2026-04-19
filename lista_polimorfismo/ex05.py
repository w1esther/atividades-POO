class Veiculo:

    def mover(self):
        return 'Veículo se movendo'
    
class Moto(Veiculo):

    def mover(self):
        return 'Moto Empinando'

class Carro(Veiculo):

    def mover(self):
        return 'Carro acelerado'

class Bicicleta(Veiculo):

    def mover(self):
        return 'Bicicleta pedalando'
    
v1 = Carro()
v2 = Moto()
v3 = Bicicleta()

lista_veiculos = [v1, v2, v3]

for veiculo in lista_veiculos:
    print(veiculo.mover())