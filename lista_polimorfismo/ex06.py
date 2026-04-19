from abc import ABC, abstractmethod
from math import pi

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = float(raio)

    def calcular_area(self):
        area = pi * self.raio * self.raio
        return f'Area Círculo: {area}'

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = float(largura)
        self.altura = float(altura)

    def calcular_area(self):
        area = self.largura * self.altura
        return f'Area Retangulo: {area}'

class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return f'Area Triângulo: {area}'
    
c1 = Circulo(3)
r1 = Retangulo(3, 4)
t1 = Triangulo(2, 5)

lista_figuras_planas = [c1, r1, t1]

for figura_plana in lista_figuras_planas:
    print(figura_plana.calcular_area())
    print(30*'-')