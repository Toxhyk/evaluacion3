from database import get_db
from utils import hash_password

def inicializar_datos():
    db = get_db()

    # Usuarios base
    if db.usuarios.count_documents({}) == 0:
        db.usuarios.insert_many([
            {"username": "admin", "password": hash_password("admin123"), "role": "admin"},
            {"username": "vendedor1", "password": hash_password("venta123"), "role": "vendedor"},
        ])

    # Productos (stock)
    if db.salmon.count_documents({}) == 0:
        db.salmon.insert_many([
            {"tipo": "Atlantico", "precio_venta": 5000, "costo": 3000, "stock": 100},
            {"tipo": "Nordico", "precio_venta": 7000, "costo": 4500, "stock": 100},
            {"tipo": "Pacifico", "precio_venta": 3000, "costo": 1500, "stock": 100},
        ])
