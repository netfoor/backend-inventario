from fastapi import APIRouter
from app.database import db
from app.models.persona import Persona

router = APIRouter()

@router.get("/")
def get_personas():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM personas")
    records = cursor.fetchall()
    return {"status": "ok", "data": records}

@router.post("/")
def create_persona(persona: Persona):
    query = """
    INSERT INTO personas (nombre, apellido_paterno, apellido_materno, puesto, telefono, email) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (persona.nombre, persona.apellido_paterno, persona.apellido_materno, persona.puesto, persona.telefono, persona.email)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Persona agregada"}

@router.put("/{id}")
def update_persona(id: int, persona: Persona):
    query = """
    UPDATE personas SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, puesto=%s, telefono=%s, email=%s, fecha_actualizacion=%s 
    WHERE id=%s
    """
    values = (persona.nombre, persona.apellido_paterno, persona.apellido_materno, persona.puesto, persona.telefono, persona.email, persona.fecha_actualizacion, id)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Persona actualizada"}

@router.delete("/{id}")
def delete_persona(id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM personas WHERE id = %s", (id,))
    db.commit()
    return {"status": "ok", "message": "Persona eliminada"}
