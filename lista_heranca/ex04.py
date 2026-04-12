class BaseForma:
    
    def area(self):
        return 0
    
class Retangulo(BaseForma):

    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def area(self):
        
        area = self.base *self.altura
        return area
    
r = Retangulo(5, 3)
print(r.area())