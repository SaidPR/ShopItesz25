#Importamos la clase
from pymongo import MongoClient

# Variable que nos indique la BD
DATABASE_URL = 'mongodb://localhost:27017'
DATABASE_NAME = 'ShopiteszRest'

class Conexion():
    def __init__(self):
        self.cliente = MongoClient(DATABASE_URL)
        self.db = self.cliente[DATABASE_NAME]
    # Cerrar conexion
    def cerrar(self):
        self.cliente.close()
    # Obtener BD
    def getDB(self):
        return self.db

