import uvicorn
from fastapi import FastAPI

# Crear una instancia de la clase FastApi
app = FastAPI()

@app.get("/")
async  def home():
     salida = {"mensaje": "Bienvenido a PEDIDOSREST"}
     return salida

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', reload = True)
