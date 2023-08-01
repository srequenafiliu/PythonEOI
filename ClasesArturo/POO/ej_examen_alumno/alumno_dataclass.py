from dataclasses import dataclass, field
from examen_dataclass import Examen

@dataclass
class Alumno:
    _nombre: str
    _curso: str
    _examenes: list[Examen] = field(default_factory=list)
    
    def add_examenes(self, *examenes):
        self._examenes.extend(examenes)

    @property
    def nombre(self):
        return self._nombre
    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self, curso):
        if not curso:
            raise ValueError("ERROR: El curso no puede estar vacío")
        self._curso = curso
    
    @property
    def media(self):
        return sum([j.nota for j in self._examenes])/len(self._examenes)
    
    def print_media_asignaturas(self):
        asignaturas = {e.asignatura for e in self._examenes}
        print("Media de las asignaturas:")
        for a in asignaturas:
            notas = [e.nota for e in self._examenes if e.asignatura == a]
            print(f"· {a}: {sum(notas)/len(notas):.2f}")
    
    def print_eficiencia(self):
        aprobados = len([e.nota for e in self._examenes if e.nota >= Examen.aprobado])
        print(f"Exámenes aprobados: {aprobados}")
        print(f"Exámenes suspendidos: {len(self._examenes)-aprobados}")
        print(f"Porcentaje de aprobados: {aprobados/len(self._examenes)*100:.2f}%")
    
    @staticmethod
    def crear_novato(nombre):
        return Alumno(nombre, "1ESO")