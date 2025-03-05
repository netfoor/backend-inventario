from fastapi import APIRouter
from app.database import db
from app.models.inventario import Inventario

router = APIRouter()

@router.get("/")
def get_inventarios():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM inventarios")
    records = cursor.fetchall()
    return {"status": "ok", "data": records}

@router.post("/")
def create_inventario(inventario: Inventario):
    query = """
    INSERT INTO inventarios (nombre, fechas, responsable, fecha_registro, estado) 
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (inventario.nombre, inventario.fechas, inventario.responsable, inventario.fecha_registro, inventario.estado)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Inventario agregado"}

@router.put("/{id}")
def update_inventario(id: int, inventario: Inventario):
    query = """
    UPDATE inventarios SET nombre=%s, fechas=%s, responsable=%s, fecha_registro=%s, estado=%s 
    WHERE id=%s
    """
    values = (inventario.nombre, inventario.fechas, inventario.responsable, inventario.fecha_registro, inventario.estado, id)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Inventario actualizado"}

@router.delete("/{id}")
def delete_inventario(id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM inventarios WHERE id = %s", (id,))
    db.commit()
    return {"status": "ok", "message": "Inventario eliminado"}
