from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import ubicacion, persona, articulo, inventario, asignacion

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye tus rutas
app.include_router(ubicacion.router, prefix="/ubicaciones", tags=["Ubicaciones"])
app.include_router(persona.router, prefix="/personas", tags=["Personas"])
app.include_router(articulo.router, prefix="/articulos", tags=["Articulos"])
app.include_router(inventario.router, prefix="/inventarios", tags=["Inventarios"])
app.include_router(asignacion.router, prefix="/asignaciones", tags=["Asignaciones"])

@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente"}
