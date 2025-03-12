from fastapi import APIRouter
from database import db
from ..models.persona import Persona
from bson import ObjectId

router = APIRouter()

@router.get("/")
def get_personas():
    personas = list(db.personas.find())
    for persona in personas:
        persona["_id"] = str(persona["_id"])
    return {"status": "ok", "data": personas}

@router.post("/")
def create_persona(persona: Persona):
    persona_dict = persona.dict()
    result = db.personas.insert_one(persona_dict)
    return {"status": "ok", "message": "Persona agregada", "id": str(result.inserted_id)}

@router.put("/{id}")
def update_persona(id: str, persona: Persona):
    result = db.personas.update_one({"_id": ObjectId(id)}, {"$set": persona.dict()})
    if result.modified_count == 1:
        return {"status": "ok", "message": "Persona actualizada"}
    else:
        return {"status": "error", "message": "Persona no encontrada"}

@router.delete("/{id}")
def delete_persona(id: str):
    result = db.personas.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"status": "ok", "message": "Persona eliminada"}
    else:
        return {"status": "error", "message": "Persona no encontrada"}
