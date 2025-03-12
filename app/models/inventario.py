from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class Inventario(BaseModel):
    id: Optional[int] = Field(default=None, alias="_id")
    nombre: str = Field(...)
    fechas: str = Field(...)
    responsable: str = Field(...)
    fecha_registro: str = Field(...)
    estado: bool = Field(...)

