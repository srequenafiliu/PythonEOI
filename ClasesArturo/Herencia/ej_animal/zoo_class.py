from animal_class import Animal

class Zoo:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.__animales: list[Animal] = list()
    
    def add_animales(self, *animales):
        self.__animales.extend(animales)

    def print_animales(self):
        for a in self.__animales:
            print(f"{a} ({a.tipo_animal()})")
    
    @property
    def num_animales (self):
        return len(self.__animales)
    
    def get_cantidad(self, tipo_animal):
        return len([j for j in self.__animales if j.tipo_animal() == tipo_animal])