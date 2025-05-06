import pymongo
import pymongo.errors

Mongo_Host = "localhost"
Mongo_Puerto = "27017"
Mongo_Tiempo_Fuera = 1000
Mongo_Uri = f"mongodb://{Mongo_Host}:{Mongo_Puerto}/"

# Variable global para conexión
cliente = None
db = None

def get_db():
    global cliente, db
    if not cliente:
        try:
            cliente = pymongo.MongoClient(Mongo_Uri, serverSelectionTimeoutMS=Mongo_Tiempo_Fuera)
            cliente.server_info()  # Verificar conexión
            db = cliente["acme_salmon"]
            print("✅ Conexión a MongoDB exitosa.")
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("❌ Tiempo excedido: " + str(errorTiempo))
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("❌ Fallo al conectarse a MongoDB: " + str(errorConexion))
    return db
