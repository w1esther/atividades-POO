class Animal:

    def emitir_som(self):
        return 'Algum sonm genérico'
    
class Gato(Animal):
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        # som_base = super().emitir_som()
        # print(som_base)
        return f'Miado de {self.nome}'
    
class Cachorro(Animal):
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return f'Latido de {self.nome}'
    
c1 = Cachorro('Bob')
c2 = Cachorro('Tom')
g1 = Gato('Alfredo')
g2 = Gato('Bartolomeu')
a1 = Animal()
a2 = Animal()

lista_animais = [c1, c2, g1, g2, a1, a2]

for animal in lista_animais:
    print(animal.emitir_som())