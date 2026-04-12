class Animal:
    def __init__(self, grupo):
        self.grupo = str(grupo)

    def fazer_som(self):
        return 'Som Animal'

class Cachorro(Animal):
    def __init__(self):
        super().__init__('mamífero')

    def fazer_som(self):
        return 'Latido'
    
c = Cachorro()
print(c.fazer_som())
