from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

# Modelo de Persona para MongoDB
class Persona(BaseModel):
    id: Optional[int] = Field(default=None, alias="_id")
    nombre: str = Field(...)
    apellido_paterno: str = Field(...)
    apellido_materno: str = Field(...)
    puesto: str = Field(...)
    telefono: str = Field(...)
    email: str = Field(...)
    fecha_actualizacion: Optional[datetime] = None
