from abc import ABC, abstractmethod

class Controlavel(ABC):

    @abstractmethod
    def mover(self):
        pass

class Jogador(Controlavel):

    def mover(self):
        return 'Jogador se movendo'
    
class Volante(Controlavel):

    def mover(self):
        return 'Volante Girando'
    
j1 = Jogador()
v1 = Volante()

lista_controlaveis = [j1, v1]

for controlavel in lista_controlaveis:
    print(controlavel.mover())