from fastapi import APIRouter
from database import db
from ..models.asignacion import Asignacion
from bson import ObjectId

router = APIRouter()

@router.get("/")
def get_asignaciones():
    asignaciones = list(db.asignaciones.find())
    for asignacion in asignaciones:
        asignacion["_id"] = str(asignacion["_id"])
    return {"status": "ok", "data": asignaciones}

@router.post("/")
def create_asignacion(asignacion: Asignacion):
    result = db.asignaciones.insert_one(asignacion.dict())
    inserted_id = str(result.inserted_id)
    return {"status": "ok", "message": "Asignación agregada", "id": inserted_id}

@router.put("/{id}")
def update_asignacion(id: str, asignacion: Asignacion):
    db.asignaciones.update_one({"_id": ObjectId(id)}, {"$set": asignacion.dict()})
    return {"status": "ok", "message": "Asignación actualizada"}

@router.delete("/{id}")
def delete_asignacion(id: str):
    db.asignaciones.delete_one({"_id": ObjectId(id)})
    return {"status": "ok", "message": "Asignación eliminada"}
