from database import get_db
from utils import check_password

def login():
    db = get_db()
    username = input("Usuario: ")
    password = input("Contraseña: ")

    user = db.usuarios.find_one({"username": username})
    if user and check_password(password, user["password"]):
        print(f"\nBienvenido, {username} ({user['role']})")
        return user
    else:
        print("Credenciales incorrectas.")
        return None
