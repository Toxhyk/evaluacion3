import bcrypt
import os

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
