'''
Crea una aplicación que acceda a una base de datos SQLite, que tendrá una tabla llamada 'tarea' con los siguientes campos:
- id INTEGER PRIMARY KEY
- descripcion TEXT 
- realizada INTEGER

Crea un menú que ofrezca las siguientes opciones:
1) Ver tareas
2) Añadir tarea
3) Marcar tarea como realizada
4) Borrar tarea
0) Salir

- Cada opción llamará a una función y le pasará la variable con el objeto de la conexión (db). Dentro de la función crea el cursor
y haz la operación correspondiente
- Las opciones 3 y 4 mostrarán las tareas actuales antes de preguntar qué tarea modificar o eliminar
- Pide al usuario la información que necesites por consola
- Por defecto todas las tareas se crean con el valor realizada a 0 (FALSE)
'''
import sqlite3
import os
from modelo.tarea import Tarea
from dao.tarea_dao import TareaDao

db = sqlite3.connect(os.path.dirname(__file__) + "/../bbdd/tareas.db")
tareaDao = TareaDao(db)

def crear_tabla(db: sqlite3.Connection):
    cursor = db.cursor()
    create_table_query = """
    DROP TABLE IF EXISTS tarea;

    CREATE TABLE tarea (
        id INTEGER PRIMARY KEY,
        descripcion TEXT,
        realizada INTEGER
    );
    """
    cursor.executescript(create_table_query)

def print_tareas(tareas: list[Tarea]):
    for t in tareas:
        print(f"{t.id}. {t.descripcion} - {'Realizada' if t.realizada else 'Sin realizar'}")

# crear_tabla(db) # Método para crear la tabla tarea

opcion = None
while opcion != '0':
    print('''
    1) Ver tareas
    2) Añadir tarea
    3) Marcar tarea como realizada
    4) Borrar tarea
    0) Salir
    ''')
    opcion = input('Seleccione una opción: ')
    match opcion:
        case "1":
            print_tareas(tareaDao.get_all())
        case "2":
            descripcion = input('Introduzca la descripción de la nueva tarea: ')
            tareaDao.insert(Tarea.create(descripcion))
        case "3":
            tareas = [t for t in tareaDao.get_all() if t.realizada == 0]
            print_tareas(tareas)
            id = input('Introduzca el ID de la tarea que ha realizado: ')
            try:
                id = int(id)
                if id in [t.id for t in tareas]:
                    tareaDao.set_realizada(id)
                    # tarea = tareaDao.get(id)
                    # tarea.realizada = 1
                    # tareaDao.update(tarea)
                    print("Tarea actualizada")
                else:
                    print("La tarea seleccionada no existe o ya fue realizada")
            except:
                print("ERROR. El valor introducido no es un número")
        case "4":
            tareas = tareaDao.get_all()
            print_tareas(tareas)
            id = input('Introduzca el ID de la tarea que desea eliminar: ')
            try:
                id = int(id)
                if id in [t.id for t in tareas]:
                    tareaDao.delete(id)
                    print("Tarea borrada")
                else:
                    print("La tarea seleccionada no existe")
            except:
                print("ERROR. El valor introducido no es un número")
        case _:
            print('Hasta pronto :)' if opcion == "0" else 'Opción no válida')