class Examen:
    aprobado = 5
    def __init__(self, asignatura: str, nota: float) -> None:
        self.__asignatura = asignatura
        self.nota = nota
    def __repr__(self) -> str:
        return f"Examen de {self.asignatura}. Nota: {self.nota:.2f} ({'Aprobado' if self.nota >= Examen.aprobado else 'Suspendido'})"
    # Getters y setters
    @property
    def asignatura(self):
        return self.__asignatura
    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("ERROR: La nota debe ser un número entre 0 y 10")
        self.__nota = nota