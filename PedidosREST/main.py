import uvicorn
from fastapi import FastAPI
from router import pedidosROUTER, productosROUTER, usuariosROUTER

# Crear una instancia de la clase FastApi
app = FastAPI()
app.include_router(pedidosROUTER.router)
app.include_router(productosROUTER.router)
app.include_router(usuariosROUTER.router)

@app.get("/")
async  def home():
     salida = {"mensaje": "Bienvenido a PEDIDOSREST"}
     return salida

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', reload = True)
