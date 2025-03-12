from fastapi import APIRouter
from database import db
from ..models.ubicacion import Ubicacion
from pymongo import MongoClient

router = APIRouter()

collection = db.ubicaciones

@router.get("/")
def get_ubicaciones():
    ubicaciones = list(collection.find({}, {'_id': 0}))
    return {"status": "ok", "data": ubicaciones}

@router.post("/")
def create_ubicacion(ubicacion: Ubicacion):
    ubicacion_data = ubicacion.dict()
    collection.insert_one(ubicacion_data)
    return {"status": "ok", "message": "Ubicación agregada"}

@router.put("/{id}")
def update_ubicacion(id: int, ubicacion: Ubicacion):
    ubicacion_data = ubicacion.dict()
    result = collection.update_one({"id": id}, {"$set": ubicacion_data})
    if result.modified_count > 0:
        return {"status": "ok", "message": "Ubicación actualizada"}
    else:
        return {"status": "error", "message": "Ubicación no encontrada"}

@router.delete("/{id}")
def delete_ubicacion(id: int):
    result = collection.delete_one({"id": id})
    if result.deleted_count > 0:
        return {"status": "ok", "message": "Ubicación eliminada"}
    else:
        return {"status": "error", "message": "Ubicación no encontrada"}
