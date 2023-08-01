from examen_dataclass import Examen
class Alumno:
    def __init__(self, nombre: str, curso: str):
        self.__nombre = nombre
        self.curso = curso
        self.__examenes = list()
    
    def add_examenes(self, *examenes):
        self.__examenes.extend(examenes)
    
    def __repr__(self) -> str:
        return f"{self.__nombre}\n· Curso: {self.__curso}\n· Exámenes:\n"+'\n'.join([('  - '+str(j)) for j in self.__examenes])
    # Getters y setters
    @property
    def nombre(self):
        return self.__nombre
    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self, curso):
        if not curso:
            raise ValueError("ERROR: El curso no puede estar vacío")
        self.__curso = curso
    
    @property
    def media(self):
        return sum([j.nota for j in self.__examenes])/len(self.__examenes)
    
    def print_media_asignaturas(self):
        ex_dict = dict()
        for e in self.__examenes:
            if not e.asignatura in ex_dict:
                ex_dict[e.asignatura] = [e.nota]
            else:
                ex_dict[e.asignatura].append(e.nota)
        print("Media de las asignaturas:")
        for e in ex_dict.keys():
            print(f"· {e}: {sum(ex_dict[e])/len(ex_dict[e]):.2f}")
    
    def print_media_asignaturas_2(self):
        asignaturas = {e.asignatura for e in self.__examenes}
        print("Media de las asignaturas:")
        for a in asignaturas:
            notas = [e.nota for e in self.__examenes if e.asignatura == a]
            print(f"· {a}: {sum(notas)/len(notas):.2f}")
    
    def print_eficiencia(self):
        aprobados = len([e.nota for e in self.__examenes if e.nota >= Examen.aprobado])
        print(f"Exámenes aprobados: {aprobados}")
        print(f"Exámenes suspendidos: {len(self.__examenes)-aprobados}")
        print(f"Porcentaje de aprobados: {aprobados/len(self.__examenes)*100:.2f}%")
    
    @staticmethod
    def crear_novato(nombre):
        return Alumno(nombre, "1ESO")