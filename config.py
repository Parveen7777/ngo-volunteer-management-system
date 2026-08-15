import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ngo_secret_key')
    DATABASE = os.path.join('database', 'ngo.db')
