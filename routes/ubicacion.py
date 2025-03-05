from fastapi import APIRouter
from app.database import db
from app.models.ubicacion import Ubicacion

router = APIRouter()

@router.get("/")
def get_ubicaciones():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ubicaciones")
    records = cursor.fetchall()
    return {"status": "ok", "data": records}

@router.post("/")
def create_ubicacion(ubicacion: Ubicacion):
    query = """
    INSERT INTO ubicaciones (edificio, area, departamento, calle, numero, ciudad, estado, pais, fecha_actualizacion) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (ubicacion.edificio, ubicacion.area, ubicacion.departamento, ubicacion.calle, ubicacion.numero, ubicacion.ciudad, ubicacion.estado, ubicacion.pais, ubicacion.fecha_actualizacion)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Ubicación agregada"}

@router.put("/{id}")
def update_ubicacion(id: int, ubicacion: Ubicacion):
    query = """
    UPDATE ubicaciones SET edificio=%s, area=%s, departamento=%s, calle=%s, numero=%s, ciudad=%s, estado=%s, pais=%s, fecha_actualizacion=%s
    WHERE id=%s
    """
    values = (ubicacion.edificio, ubicacion.area, ubicacion.departamento, ubicacion.calle, ubicacion.numero, ubicacion.ciudad, ubicacion.estado, ubicacion.pais, ubicacion.fecha_actualizacion, id)
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    return {"status": "ok", "message": "Ubicación actualizada"}

@router.delete("/{id}")
def delete_ubicacion(id: int):
    cursor = db.cursor()
    cursor.execute("DELETE FROM ubicaciones WHERE id = %s", (id,))
    db.commit()
    return {"status": "ok", "message": "Ubicación eliminada"}
