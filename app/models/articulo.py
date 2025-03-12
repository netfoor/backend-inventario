from typing import Optional
from pydantic import BaseModel, Field

class Articulo(BaseModel):
    id: Optional[int] = Field(default=None, alias="_id")
    tipo: str
    nombre: str
    descripcion: str
    estado: str
    ubicacion_id: int
    fecha_actualizacion: str