from dataclasses import dataclass
from sqlite3 import Connection
from modelo.producto import Producto

@dataclass
class ProductoDao:
    db: Connection

    @staticmethod
    def product_factory(cursor, row):
        return Producto(row[0], row[1], row[2])
    
    def get_all(self) -> list[Producto]:
        self.db.row_factory = ProductoDao.product_factory
        return self.db.cursor().execute("SELECT * FROM producto").fetchall()
    
    def get(self, id: int) -> Producto:
        self.db.row_factory = ProductoDao.product_factory
        return self.db.cursor().execute("SELECT * FROM producto WHERE id = ?", (id,)).fetchone()
    
    def insert(self, producto: Producto) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO producto(nombre, precio) VALUES(?, ?)",
                (producto.nombre, producto.precio)
            )
            producto.id = cursor.lastrowid if cursor.lastrowid else 1
    
    def update(self, producto: Producto) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute(
                "UPDATE producto SET nombre = ?, precio = ? WHERE id = ?",
                (producto.nombre, producto.precio, producto.id)
            )

    def delete(self, id: int) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM producto WHERE id = ?", (id,))