class Animal:
    def __init__(self, nombre: str, peso: float) -> None:
        self.nombre = nombre
        self.peso = peso
    def comer(self) -> None:
        self.peso *= 1.05

class Mamifero(Animal):
    def __init__(self, nombre, peso, herbivoro: bool) -> None:
        super().__init__(nombre, peso)
        self.herbivoro = herbivoro
    
    # Método sobreescrito
    def comer(self):
        super().comer()
        print(f"\'{self.nombre}\' ha comido {'hierba' if self.herbivoro else 'carne'}")

animal1 = Mamifero("Conejo", 40, True)
animal2 = Mamifero("Lobo", 60, False)

animal1.comer()
print(f"Nuevo peso: {animal1.peso}")
animal2.comer()
print(f"Nuevo peso: {animal2.peso}")
