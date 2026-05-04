from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self.__velocidade_max = None
        self.velocidade_max = velocidade

    @property
    def velocidade_max(self):
        return self.__velocidade_max
    
    @velocidade_max.setter
    def velocidade_max(self, velocidade):
        if velocidade < 0:
            print('Velocidade não pode ser negativa!')
        else:
            self.__velocidade_max = velocidade

    @abstractmethod
    def calcular_tempo_viagem(self, distancia):
        pass

class Manutencao(ABC):

    @abstractmethod
    def calcular_custo_manutencao(self):
        pass

class Carro(Veiculo, Manutencao):
    def __init__(self, modelo, velocidade, consumo_combustivel):
        super().__init__(modelo, velocidade)
        self.consumo_combustivel_kmh = consumo_combustivel

    def calcular_tempo_viagem(self, distancia):
        tempo_viagem = distancia/self.velocidade_max
        return tempo_viagem
    
    def calcular_custo_manutencao(self):
        custo_manutencao_fixo = 500
        return custo_manutencao_fixo
    
class Moto(Veiculo, Manutencao):
    def __init__(self, modelo, velocidade, consumo_combustivel):
        super().__init__(modelo, velocidade)
        self.consumo_combustivel_kmh = consumo_combustivel

    def calcular_tempo_viagem(self, distancia):
        tempo_viagem = distancia/self.velocidade_max
        return tempo_viagem
    
    def calcular_custo_manutencao(self):
        custo_manutencao_fixo = 200
        return custo_manutencao_fixo
    
class Aviao(Veiculo, Manutencao):
    def __init__(self, modelo, velocidade, consumo_combustivel, altitude_max):
        super().__init__(modelo, velocidade)
        self.consumo_combustivel_kmh = consumo_combustivel
        self.altitude_max = altitude_max

    def calcular_tempo_viagem(self, distancia):
        tempo_viagem = distancia/self.velocidade_max
        return tempo_viagem
    
    def calcular_custo_manutencao(self):
        custo_manutencao_fixo = 5000
        return custo_manutencao_fixo
    
class Motorista:
    def __init__(self, nome, cnh):
        self.nome = nome
        self.cnh = cnh

class Viagem:
    def __init__(self, motorista, veiculo, distancia):
        self.motorista = motorista
        self.veiculo = veiculo
        self.distancia = distancia

    def resumo_viagem(self):
        tempo = self.veiculo.calcular_tempo_viagem(self.distancia)

        return (
        f"Motorista: {self.motorista.nome}\n"
        f"Veículo: {self.veiculo.modelo}\n"
        f"Distância: {self.distancia} km\n"
        f"Tempo estimado: {tempo:.2f} horas"
        )
    
class Frota():
    def __init__(self):
        self.lista_veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.lista_veiculos.append(veiculo)
    
    def listar_veiculos(self):
        for veiculo in self.lista_veiculos:
            print(veiculo.modelo)

carro1 = Carro('Onix', 80, 10)
aviao1 = Aviao('azul', 200, 30, 5000)
moto1 = Moto('Trail', 100, 5)

lista_veiculos = [carro1, aviao1, moto1]

for veiculo in lista_veiculos:
    print(veiculo.calcular_tempo_viagem(100))

# 🔹 Teste da frota (composição)
print("\n=== FROTA ===")
frota = Frota()
frota.adicionar_veiculo(carro1)
frota.adicionar_veiculo(aviao1)
frota.adicionar_veiculo(moto1)

frota.listar_veiculos()


# 🔹 Teste da viagem (agregação)
print("\n=== VIAGEM ===")
motorista1 = Motorista('Maria', '123456')

viagem1 = Viagem(motorista1, carro1, 150)
print(viagem1.resumo_viagem())


# 🔹 Teste de custo de manutenção
print("\n=== MANUTENÇÃO ===")
for veiculo in lista_veiculos:
    print(f'{veiculo.modelo}: R$ {veiculo.calcular_custo_manutencao()}')


# # 🔹 (Opcional) Teste do custo total da viagem
# print("\n=== CUSTO TOTAL DA VIAGEM ===")
# print(f'R$ {viagem1.calcular_custo_total():.2f}')