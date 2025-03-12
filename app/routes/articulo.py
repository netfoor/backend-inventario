from fastapi import APIRouter
from database import db
from ..models.articulo import Articulo
from pymongo import MongoClient

router = APIRouter()

collection = db.articulos

@router.get("/")
def get_articulos():
    articulos = list(collection.find())
    for articulo in articulos:
        articulo['_id'] = str(articulo['_id'])
    return {"status": "ok", "data": articulos}

@router.post("/")
def create_articulo(articulo: Articulo):
    articulo_data = articulo.dict()
    result = collection.insert_one(articulo_data)
    return {"status": "ok", "message": "Artículo agregado", "inserted_id": str(result.inserted_id)}
