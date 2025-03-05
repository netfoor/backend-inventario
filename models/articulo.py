from pydantic import BaseModel
from typing import Optional

class Articulo(BaseModel):
    id: Optional[int] = None
    tipo: str  
    nombre: str
    descripcion: str
    estado: str  
    ubicacion_id: int  
    fecha_actualizacion: str
