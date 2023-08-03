from dataclasses import dataclass

@dataclass
class Producto:
    id:int
    nombre: str
    precio: float

    @staticmethod
    def create(nombre, precio):
        return Producto(0, nombre, precio)
