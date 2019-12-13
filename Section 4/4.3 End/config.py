import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 
        'db' : 'todo_app',
        'username':'josephaws',
        'password':'josephaws1234',
        'host': 'ds047792.mlab.com',
        'port': 47792
    }


    