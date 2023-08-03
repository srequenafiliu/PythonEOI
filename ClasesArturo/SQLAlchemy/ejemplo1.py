from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Numeric, create_engine, select

class BaseModel(DeclarativeBase):
    pass

class Producto(BaseModel):
    __tablename__ = "producto"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10, 2))

    def __repr__(self) -> str:
        return f"{self.id} - {self.nombre} ({self.precio:.2f} €)"
    
engine = create_engine("sqlite:///ClasesArturo/SQLAlchemy/bbdd/datos.db", echo=True)
BaseModel.metadata.create_all(engine)

def add_productos():
    silla = Producto(nombre ="Silla", precio = 25)
    mesa = Producto(nombre ="Mesa", precio = 99.95)
    estanteria = Producto(nombre ="Estantería", precio = 60.5)

    # expire_on_commit=False -> Permite acceder a los objetos fuera de la sesión
    with Session(engine, expire_on_commit=False) as session:
        session.add(silla)
        session.add_all([mesa, estanteria])
        session.commit()
    print(silla, mesa, estanteria)

def mostrar_productos():
    with Session(engine) as session:
        st = select(Producto)
        productos = session.execute(st).scalars().all()
        print(productos)

        st2 = select(Producto).where(Producto.precio>50)
        productos2 = session.execute(st2).scalars().all()
        print(productos2)

        st3 = select(Producto).where(Producto.id == 10)
        '''
        first() -> Devuelve el primer relustado o None si no hay
        one_or_none() -> Devuelve el único resultado, None si no hay. Error si hay más de un resultado
        one() -> Devuelve el único resultado. Error si no hay o hay más de uno
        '''
        producto = session.execute(st3).scalars().one_or_none()
        print(producto)

        producto2 = session.get(Producto, 2)
        print(producto2)

        st4 = select(Producto.nombre, Producto.precio)
        nombres = session.execute(st4).all()
        for n, p in nombres:
            print(f"{n} - {float(p):.2f}€")

def modificar_productos():
    with Session(engine) as session:
        producto = session.get(Producto, 3)
        if producto:
            producto.nombre = "Modificado"
            producto.precio = 11
            session.commit()
        else:
            print("No se ha encontrado el producto")

def borrar_productos():
    with Session(engine) as session:
        producto = session.get(Producto, 3)
        session.delete(producto)
        print(session.deleted)

add_productos()
# modificar_productos()
# borrar_productos()
mostrar_productos()