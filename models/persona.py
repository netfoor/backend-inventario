from pydantic import BaseModel
from typing import Optional

# Modelo de Persona
class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    puesto: str
    telefono: str
    email: str