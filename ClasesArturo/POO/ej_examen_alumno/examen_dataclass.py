from dataclasses import dataclass
@dataclass
class Examen:
    _asignatura: str
    _nota: float
    aprobado = 5 # Atributo de clase porque no se especifica tipo

    @property
    def asignatura(self):
        return self._asignatura
    @property
    def nota(self):
        return self._nota
    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("ERROR: La nota debe ser un número entre 0 y 10")
        self._nota = nota