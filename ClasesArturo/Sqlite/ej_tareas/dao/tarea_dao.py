from dataclasses import dataclass
from sqlite3 import Connection
from modelo.tarea import Tarea

@dataclass
class TareaDao:
    db: Connection

    @staticmethod
    def product_factory(cursor, row):
        return Tarea(row[0], row[1], bool(row[2]))
    
    def get_all(self) -> list[Tarea]:
        self.db.row_factory = TareaDao.product_factory
        return self.db.cursor().execute("SELECT * FROM tarea").fetchall()
    
    def get(self, id: int) -> Tarea:
        self.db.row_factory = TareaDao.product_factory
        return self.db.cursor().execute("SELECT * FROM tarea WHERE id = ?", (id,)).fetchone()

    def insert(self, tarea: Tarea) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO tarea(descripcion, realizada) VALUES(?, ?)",
                (tarea.descripcion, tarea.realizada)
            )
            tarea.id = cursor.lastrowid if cursor.lastrowid else 1

    def update(self, tarea: Tarea) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute(
                "UPDATE tarea SET descripcion = ?, realizada = ? WHERE id = ?",
                (tarea.descripcion, tarea.realizada, tarea.id)
            )

    def set_realizada(self, id: int) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute("UPDATE tarea SET realizada = 1 WHERE id = ?", (id,))


    def delete(self, id: int) -> None:
        with self.db as db:
            cursor = db.cursor()
            cursor.execute("DELETE FROM tarea WHERE id = ?", (id,))