class Cuadrado:
    def __init__(self, lado):
        self.__lado = lado
    def __repr__(self) -> str:
        return f"Cuadrado (lado {self.__lado})"
    get_area = lambda self: self.__lado**2
    def __add__(self, other):
        return Cuadrado(self.__lado + other.__lado) # Llama a __srt__
    # Comparadores
    def __eq__(self, other) -> bool:
        return self.__lado == other.__lado
    def __ne__(self, other) -> bool:
        return self.__lado != other.__lado
    def __gt__(self, other) -> bool:
        return self.__lado > other.__lado
    def __lt__(self, other) -> bool:
        return self.__lado < other.__lado
    def __ge__(self, other) -> bool:
        return self.__lado >= other.__lado
    def __le__(self, other) -> bool:
        return self.__lado <= other.__lado
    ''' Getter y setter estilo Java
    def get_lado(self):
        return self.__lado
    def set_lado(self, lado):
        if lado <= 0:
            raise ValueError("El cuadrado no puede tener lado negativo")
        self.__lado = lado
    '''
    @property # Indica que 'lado' es una propiedad de acceso público (llama a esta función implícita)
    def lado(self):
        return self.__lado
    @lado.setter
    def lado(self, lado):
        if lado <= 0:
            raise ValueError("El cuadrado no puede tener lado negativo")
        self.__lado = lado
    @property
    def area(self):
        return self.__lado**2

c = Cuadrado(8)
print(type(c))
## print('Lado:', c.__lado) Da error
print('Lado:', c.lado)
print('Área:', c.get_area())
print(c)

c2 = Cuadrado(14)
c3 = c+c2
print(c3)
print(c < c2)
print(c > c2)

lista = [c3, c2, c]
lista.sort()
print(lista)

c = Cuadrado(4)
print('Lado:', c.lado)
print('Área:', c.area)
## c.lado -= 20 Salta el ValueError
c.lado += 2
print("Nuevo lado:", c.lado)
print('Nueva área:', c.area)