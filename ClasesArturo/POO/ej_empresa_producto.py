'''
Crea una clase llamada Producto con los atributos: referencia, nombre, precio y stock
Crea una clase llamada Empresa con los atributos: nombre, (lista de productos)
Crea el método __repr__ en la clase Producto y en la clase Empresa (mostrará el nombre de la empresa y cada producto en una línea separada)
Crea el método total_productos en la clase Empresa que devuelva el total de productos en su almacén (suma de producto*stock)
Crea una empresa con un listado de al menos 4 productos y prueba la llamada a los métodos anteriores
No hace falta crear propiedades (getter/setter) si no las necesitas desde fuera de la clase
'''
class Producto:
    def __init__(self, referencia, nombre, precio, stock) -> None:
        self.__referencia = referencia
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    def __repr__(self) -> str:
        return f"{self.__nombre} (Referencia: {self.__referencia})\n· Precio: {self.__precio:.2f}€\n· Stock: {self.__stock}"
    @property # Se usa el getter en total_productos
    def stock(self):
        return self.__stock

class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__productos = list()
    def add_productos(self, *productos):
        self.__productos.extend(productos)
    def __repr__(self) -> str:
        return f"{self.__nombre}\n"+'\n'.join([str(j) for j in self.__productos]) # join() para una lista de objetos
    @property
    def total_productos(self):
        return sum([j.stock for j in self.__productos])

e = Empresa("Muebles El Castor")
e.add_productos(Producto(1, "Mesa", 59.95, 7), Producto(2, "Silla", 34.99, 22), Producto(3, "Armario", 84.5, 14), Producto(4, "Escritorio", 60, 15))
print(e)
print("Productos en el almacén:", e.total_productos)