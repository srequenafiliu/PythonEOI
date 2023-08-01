class Empleado:
    # __slots__ = ["nombre", "sueldo"]
    sueldo_minimo = 14000 # atributo de clase

    @classmethod
    def crea_becario(cls, nombre): # Crea empleado con sueldo mínimo
        return cls(nombre, cls.sueldo_minimo)

    @staticmethod
    def crea_becario_static(nombre):
        return Empleado(nombre, Empleado.sueldo_minimo)
    
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    def __repr__(self) -> str:
        return f"{self.nombre} - {self.sueldo:.2f}€"

e = Empleado("Pepito", 30000)
# e.sueldo_minimo = 16000
print(Empleado.sueldo_minimo)
print(e.sueldo_minimo)
'''print(e.__dict__)
print(Empleado.__dict__)'''

becario = Empleado.crea_becario("Vanessa")
becario2 = Empleado.crea_becario_static("Pedro")
print(becario)
print(becario2)