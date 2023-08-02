from animal_class import Animal

class Mamifero(Animal):
    def __init__(self, nombre, peso, carnivoro: bool) -> None:
        super().__init__(nombre, peso)
        self.carnivoro = carnivoro

    def __repr__(self) -> str:
        return super().__repr__()+f"- {'Carn' if self.carnivoro else 'Herb'}ívoro"
    
    # Método sobreescrito
    def comer(self):
        super().comer()
        print(f"\'{self.nombre}\' ha comido {'carne' if self.carnivoro else 'hierba'}")

    def tipo_animal(self):
        return "Mamífero"