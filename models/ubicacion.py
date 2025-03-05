from pydantic import BaseModel
from typing import Optional

# Modelo de Ubicación
class Ubicacion(BaseModel):
    id: Optional[int] = None
    edificio: str
    area: str
    departamento: str
    calle: str
    numero: str
    ciudad: str
    estado: str
    pais: str
    fecha_actualizacion: str