from pydantic import BaseModel
from typing import Optional

class Asignacion(BaseModel):
    id: Optional[int] = None
    persona_id: int  # FK a Persona
    articulo_id: int  # FK a Artículo
    observacion: str
    estado: bool
    fecha_inicio: str
    fecha_fin: str
    usuario_asignador: int  # FK a usuario que asignó
