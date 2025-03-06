from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Modelo de Persona
class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    puesto: str
    telefono: str
    email: str
    fecha_actualizacion: Optional[datetime] = None