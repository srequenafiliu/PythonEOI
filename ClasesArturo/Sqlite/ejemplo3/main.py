import sqlite3
import os
from modelo.producto import Producto
from dao.producto_dao import ProductoDao

db = sqlite3.connect(os.path.dirname(__file__)+"/../bbdd/productos.db")

productoDao = ProductoDao(db)

print(productoDao.get_all())

producto1 = productoDao.get(1)
print(producto1)

# pInsert = Producto.create("Insert", 100)
# productoDao.insert(pInsert)
# print(pInsert)

# producto1.nombre = "Otra modificación"
# producto1.precio = 1
# productoDao.update(producto1)

# productoDao.delete(4)

print(productoDao.get_all())