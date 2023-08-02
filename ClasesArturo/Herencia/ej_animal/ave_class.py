import random
from animal_class import Animal

class Ave(Animal):
    def __init__(self, nombre, peso, voladora: bool) -> None:
        super().__init__(nombre, peso)
        self.voladora = voladora

    def __repr__(self) -> str:
        return super().__repr__()+f" - Ave {'' if self.voladora else 'no '}voladora"
    
    def poner_huevos(self):
        huevos = random.randint(1, 6)
        self.peso -= 0.05*huevos
        print(f"\'{self.nombre}\' ha puesto {huevos} huevo{'s' if huevos>1 else ''}")
    
    def tipo_animal(self):
        return "Ave"