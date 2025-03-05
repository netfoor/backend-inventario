from pydantic import BaseModel
from typing import Optional

class Inventario(BaseModel):
    id: Optional[int] = None
    nombre: str
    fechas: str  
    responsable: str
    fecha_registro: str
    estado: bool