from fastapi import APIRouter
from database import db
from ..models.inventario import Inventario
from bson import ObjectId

router = APIRouter()

@router.get("/")
def get_inventarios():
    inventarios = list(db.inventarios.find())
    for inventario in inventarios:
        inventario["_id"] = str(inventario["_id"])
    return {"status": "ok", "data": inventarios}

@router.post("/")
def create_inventario(inventario: Inventario):
    inventario_dict = inventario.dict()
    result = db.inventarios.insert_one(inventario_dict)
    return {"status": "ok", "message": "Inventario agregado", "id": str(result.inserted_id)}

@router.put("/{id}")
def update_inventario(id: str, inventario: Inventario):
    db.inventarios.update_one({"_id": ObjectId(id)}, {"$set": inventario.dict()})
    return {"status": "ok", "message": "Inventario actualizado"}

@router.delete("/{id}")
def delete_inventario(id: str):
    db.inventarios.delete_one({"_id": ObjectId(id)})
    return {"status": "ok", "message": "Inventario eliminado"}
