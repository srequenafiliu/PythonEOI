'''
Crea una clase llamada Persona con nombre y edad (privados)
Crea las correspondientes propiedades (getter/setter) sin los guiones para obtener
y establecer los valores de nombre y edad
Controla que el nombre no esté vacío y la edad no pueda ser menor que 0
Crea una lista con 3 personas y recórrela restándole 10 a la edad de cada uno
Prueba también a cambiar el nombre de alguna persona de la lista a cadena vacía
'''

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def __repr__(self) -> str:
        return f"Persona:\n· Nombre: {self.__nombre}\n· Edad: {self.__edad}"
    # Getter/setter para nombre
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        if nombre == "":
            raise ValueError("ERROR: El nombre no puede estar vacío")
        self.__nombre = nombre
    # Getter/setter para edad
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("ERROR: La edad no puede ser un número negativo")
        self.__edad = edad

personas = [Persona("Sandra", 23), Persona("Jorge", 30), Persona("Helena", 9)]
try:
    personas[2].nombre = ""
except ValueError as e:
    print(e)
for p in personas:
    try:
        p.edad -=10
    except ValueError as e:
        print(e)
    print(p)