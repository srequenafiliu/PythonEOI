from dataclasses import dataclass

@dataclass
class Tarea:
    id:int
    descripcion: str
    realizada: bool

    @staticmethod
    def create(descripcion):
        return Tarea(0, descripcion, False)
