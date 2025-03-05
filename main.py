from fastapi import FastAPI
from app.routes import persona, ubicacion, asignacion, inventario

app = FastAPI()

# Incluir las rutas
app.include_router(persona.router, prefix="/personas", tags=["Personas"])
app.include_router(ubicacion.router, prefix="/ubicaciones", tags=["Ubicaciones"])
app.include_router(asignacion.router, prefix="/asignaciones", tags=["Asignaciones"])
app.include_router(inventario.router, prefix="/inventarios", tags=["Inventarios"])

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}
