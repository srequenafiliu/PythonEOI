from dataclasses import dataclass

@dataclass
class Direccion:
    calle: str
    numero: int
    cp: str

@dataclass
class Persona:
    nombre: str
    edad: int
    direccion: Direccion
    
dir = Direccion("Calle perdida", 23, "02434")
p = Persona("Ana", 39, dir)
p2 = Persona("Ana", 39, dir)

print(p)
print(p == p2)