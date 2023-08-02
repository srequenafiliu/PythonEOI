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

db = sqlite3.connect(os.path.dirname(__file__) + "/bbdd/tareas.db")

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

def ver_tareas(db: sqlite3.Connection, extra=""):
    cursor = db.cursor()
    tareas = cursor.execute("SELECT * FROM tarea "+extra).fetchall()
    for t in tareas:
        print(f"{t[0]}. {t[1]} - {'Realizada' if t[2]==1 else 'Sin realizar'}")
    return [t[0] for t in tareas]

def add_tarea(db: sqlite3.Connection):
    cursor = db.cursor()
    descripcion = input('Introduzca la descripción de la nueva tarea: ')
    cursor.execute("INSERT INTO tarea(descripcion, realizada) VALUES(?, ?)", (descripcion, 0))
    print(cursor.lastrowid)
    db.commit()

def tarea_realizada(db: sqlite3.Connection):
    cursor = db.cursor()
    tareas = ver_tareas(db, "WHERE realizada = 0")
    id = input('Introduzca el ID de la tarea que ha realizado: ')
    try:
        id = int(id)
        if id in tareas:
            cursor.execute("UPDATE tarea SET realizada = 1 WHERE id = ?", (id,))
            print("Tarea actualizada")
            db.commit()
        else:
            print("La tarea seleccionada no existe o ya fue realizada")
    except:
        print("ERROR. El valor introducido no es un número")


def delete_tarea(db: sqlite3.Connection):
    cursor = db.cursor()
    tareas = ver_tareas(db)
    id = input('Introduzca el ID de la tarea que desea eliminar: ')
    try:
        id = int(id)
        if id in tareas:
            cursor.execute("DELETE FROM tarea WHERE id = ?", (id,))
            print("Tarea borrada")
            db.commit()
        else:
            print("La tarea seleccionada no existe")
    except:
        print("ERROR. El valor introducido no es un número")

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
            ver_tareas(db)
        case "2":
            add_tarea(db)
        case "3":
            tarea_realizada(db)
        case "4":
            delete_tarea(db)
        case "0":
            db.close()
            print('Hasta pronto :)')
        case _:
            print('Opción no válida')