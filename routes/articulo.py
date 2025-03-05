from fastapi import APIRouter
from app.database import db
from app.models.articulo import Articulo

router = APIRouter()

@router.get("/")
def get_articulos():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM articulos")
    records = cursor.fetchall()
    return {"status": "ok", "data": records}

@router.post("/")
def create_articulo(articulo: Articulo):
    query = f"INSERT INTO articulos (tipo, nombre, descripcion, estado, ubicacion_id, fecha_actualizacion) VALUES ('{articulo.tipo}', '{articulo.nombre}', '{articulo.descripcion}', '{articulo.estado}', {articulo.ubicacion_id}, '{articulo.fecha_actualizacion}')"
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    return {"status": "ok", "message": "Artículo agregado"}
