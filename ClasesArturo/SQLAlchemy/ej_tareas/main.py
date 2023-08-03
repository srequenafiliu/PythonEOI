from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from modelo.tarea import BaseModel, Tarea

ruta = "ClasesArturo/SQLAlchemy" # Cambiar la ruta

engine = create_engine(f"sqlite:///{ruta}/bbdd/tareas.db")
BaseModel.metadata.create_all(engine)
    
def get_tareas() -> list[Tarea]:
    with Session(engine) as session:
        return list(session.execute(select(Tarea)).scalars().all())
    
def get(id: int) -> Tarea | None:
    with Session(engine) as session:
        return session.execute(select(Tarea).where(Tarea.id == id)).scalars().one_or_none()

def insert(tarea: Tarea) -> None:
    with Session(engine) as session:
        session.add(tarea)
        session.commit()

def set_realizada(id: int) -> None:
    with Session(engine) as session:
        tarea = session.get(Tarea, id)
        if tarea:
            tarea.realizada = True
            session.commit()
        else:
            print("No se ha encontrado la tarea")

def delete(id: int) -> None:
    with Session(engine) as session:
        producto = session.get(Tarea, id)
        session.delete(producto)
        session.commit()

def print_tareas(tareas: list[Tarea]):
    for t in tareas:
        print(t)

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
            if len(get_tareas()):
                print_tareas(get_tareas())
            else:
                print("Todavía no se ha guardado ninguna tarea")
        case "2":
            descripcion = input('Introduzca la descripción de la nueva tarea: ')
            insert(Tarea(descripcion = descripcion))
        case "3":
            tareas = [t for t in get_tareas() if t.realizada == 0]
            print_tareas(tareas)
            id = input('Introduzca el ID de la tarea que ha realizado: ')
            try:
                id = int(id)
                if id in [t.id for t in tareas]:
                    set_realizada(id)
                    print("Tarea actualizada")
                else:
                    print("La tarea ya estaba marcada como realizada")
            except:
                print("ERROR. El valor introducido no es un número")
        case "4":
            tareas = get_tareas()
            print_tareas(tareas)
            id = input('Introduzca el ID de la tarea que desea eliminar: ')
            try:
                id = int(id)
                if id in [t.id for t in tareas]:
                    delete(id)
                    print("Tarea borrada")
                else:
                    print("La tarea seleccionada no existe")
            except:
                print("ERROR. El valor introducido no es un número")
        case _:
            print('Hasta pronto :)' if opcion == "0" else 'Opción no válida')