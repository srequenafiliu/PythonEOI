# Clase base
class Empleado:
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo
    
    def sube_sueldo(self, porcentaje):
        self.sueldo *= 1+porcentaje/100
    
    def __repr__(self) -> str:
        return f"{self.nombre}. Sueldo: {self.sueldo:.2f}€"
    
    @property
    def sueldo_mensual(self):
        return self.sueldo / 12


# Clase derivada
class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje) -> None:
        super().__init__(nombre, sueldo) # Llamamos al constructor de Empleado
        self.lenguaje = lenguaje
    
    # Método sobreescrito
    def sube_sueldo(self, porcentaje: float):
        super().sube_sueldo(porcentaje) # Llamamos al método hereadado original
        if self.lenguaje == "Python":
            print("El programador de Python sube un 5% extra")
            self.sueldo *= 1.05

    def __repr__(self) -> str:
        return super().__repr__() + f". Lenguaje: {self.lenguaje}"
    
    @property
    def sueldo_mensual(self): # Los programadores Python cobran 100€ más al mes
        sueldo = super().sueldo_mensual
        return sueldo + 100 if self.lenguaje == "Python" else sueldo

p1 = Programador("Paco", 20000, "Python")
p1.sube_sueldo(5)
print(p1.sueldo)
print(f"Sueldo mensual de {p1.nombre}: {p1.sueldo_mensual:.2f}€")
print(p1)

p2 = Programador("Pepe", 20000, "Java")
p2.sube_sueldo(5)
print(f"Sueldo mensual de {p2.nombre}: {p2.sueldo_mensual:.2f}€")
print(p2)