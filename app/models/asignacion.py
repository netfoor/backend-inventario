from typing import Optional
from pydantic import BaseModel, Field


class Asignacion(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    persona_id: int
    articulo_id: int
    observacion: str
    estado: bool
    fecha_inicio: str
    fecha_fin: str
    usuario_asignador: int


