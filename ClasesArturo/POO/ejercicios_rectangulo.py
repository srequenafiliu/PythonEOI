'''
Crea la clase Rectangulo con dos propiedades (ancho y alto)
Crea un objeto de la clase Rectangulo
Muestra por pantalla el área del rectángulo (ancho*alto)
'''

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    get_area = lambda self: self.ancho*self.alto
    '''
    def get_area(self):
        return self.ancho*self.alto
    '''
    __repr__ = lambda self: f"Rectángulo:\n· Ancho: {self.ancho}\n· Alto: {self.alto}"
    '''
    def __repr__(self) -> str:
        return f"Rectángulo:\n· Ancho: {self.ancho}\n· Alto: {self.alto}"
    '''
    __lt__ = lambda self, other: self.get_area() < other.get_area()
    '''
    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()
    '''
r = Rectangulo(5, 4)
print(f"Área del rectángulo: {r.get_area()}")
print(r)

'''
Define el método __lt__ para indicar cuando un rectángulo es menor que otro (usa el área)
Después crea una lista con 3 0 4 rectángulos y ordénala
Recorre la lista y muestra los rectángulos que contiene con su correspondiente área
'''
lista_rectangulos = [r, Rectangulo(3, 6), Rectangulo(2, 8), Rectangulo(4, 9)]
lista_rectangulos.sort()
print('Lista de rectángulos ordenada')
for rect in lista_rectangulos:
    print(rect)
    print(f"· Área: {rect.get_area()}")