class Veiculo:
    def acelerar(self):
        print('Acelerando...')
    
class Carro(Veiculo):
    def acelerar(self):
        print('Carro acelerando...')

class Moto(Veiculo):
    def acelerar(self):
        print('Moto acelerando...')

veiculos = [Carro(), Moto()]
for veiculo in veiculos:
    veiculo.acelerar()