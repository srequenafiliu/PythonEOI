from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean

class BaseModel(DeclarativeBase):
    pass

class Tarea(BaseModel):
    __tablename__ = "tarea"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(Boolean(False), insert_default=False)

    def __repr__(self) -> str:
        return f"{self.id}. {self.descripcion} - {'Realizada' if self.realizada else 'Sin realizar'}"
