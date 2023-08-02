from abc import ABC, abstractclassmethod

class Animal(ABC):
    def __init__(self, nombre: str, peso: float) -> None:
        self.nombre = nombre
        self.peso = peso

    def __repr__(self) -> str:
        return f"{self.nombre} ({self.peso} kg)"

    def comer(self) -> None:
        self.peso *= 1.05

    @abstractclassmethod
    def tipo_animal(self):
        pass
