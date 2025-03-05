from fastapi import APIRouter
from app.database import db
from app.models.asignacion import Asignacion

router = APIRouter()

@router.get("/")
def get_asignaciones():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM asignaciones")
    records = cursor.fetchall()
    return {"status": "ok", "data": records}

@router.post("/")
def create_asignacion(asignacion: Asignacion):
    query = """
    INSERT INTO asignaciones (persona_id, articulo_id, observacion, estado, fecha_inicio, fecha_fin, usuario_asignador) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (asignacion.persona_id, asignacion.articulo_id, asignacion.observacion, asignacion.estado, asignacion.fecha_inicio, asignacion.fecha_fin, asignacion.usuario_asignador)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Asignación agregada"}

@router.put("/{id}")
def update_asignacion(id: int, asignacion: Asignacion):
    query = """
    UPDATE asignaciones SET persona_id=%s, articulo_id=%s, observacion=%s, estado=%s, fecha_inicio=%s, fecha_fin=%s, usuario_asignador=%s 
    WHERE id=%s
    """
    values = (asignacion.persona_id, asignacion.articulo_id, asignacion.observacion, asignacion.estado, asignacion.fecha_inicio, asignacion.fecha_fin, asignacion.usuario_asignador, id)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Asignación actualizada"}

@router.delete("/{id}")
def delete_asignacion(id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM asignaciones WHERE id = %s", (id,))
    db.commit()
    return {"status": "ok", "message": "Asignación eliminada"}
