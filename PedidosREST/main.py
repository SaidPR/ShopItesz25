# Importar la librería de uvicorn para usar un servidor local
import uvicorn
# Importar la clase FastAPI del framework
from fastapi import FastAPI
from contextlib import asynccontextmanager
from router import pedidosROUTER, productosROUTER, usuariosROUTER
from dao.database import Conexion

# Manejo del ciclo de vida de la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Conexión con MongoDB")
    conexion = Conexion()
    app.state.db = conexion.getDB()  # Guardamos la conexión en app.state
    yield  # Pausa aquí hasta que la app se cierre
    print("Cerrando la conexión con MongoDB")
    conexion.cerrar()

# Crear una instancia de FastAPI con el manejador de ciclo de vida
app = FastAPI(lifespan=lifespan)

# Incluir routers
app.include_router(pedidosROUTER.router)
app.include_router(productosROUTER.router)
app.include_router(usuariosROUTER.router)

@app.get("/")
async def home():
    return {"Mensaje": "Bienvenida a PEDIDOSREST"}

# Ejecutar el servidor
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)
