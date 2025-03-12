from typing import Optional
from pydantic import BaseModel, Field

class Ubicacion(BaseModel):
    id: Optional[int] = Field(default=None, alias="_id")
    edificio: str
    area: str
    departamento: str
    calle: str
    numero: str
    ciudad: str
    estado: str
    pais: str
    fecha_actualizacion: str
