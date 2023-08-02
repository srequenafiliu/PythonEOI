# Ejemplo clases abstractas
from abc import ABC, abstractclassmethod
import math

class Figura(ABC): # Clase abstracta
    @abstractclassmethod
    def get_area(self):
        pass

    @abstractclassmethod
    def get_perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto
    
    def get_area(self):
        return self.ancho*self.alto

    def get_perimetro(self):
        return (self.ancho+self.alto)*2

class Circulo(Figura):
    def __init__(self, radio) -> None:
        self.radio = radio
    
    def get_area(self):
        return math.pi * self.radio ** 2

    def get_perimetro(self):
        return math.pi * self.radio * 2

# figura = Figura()

rect = Rectangulo(4, 6)
print(f"Área del rectángulo: {rect.get_area()}")
print(f"Perímetro del rectángulo: {rect.get_perimetro()}")

circulo = Circulo(4)
print(f"Área del círculo: {circulo.get_area():.2f}")
print(f"Perímetro del círculo: {circulo.get_perimetro():.2f}")