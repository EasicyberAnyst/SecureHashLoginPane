import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'database.db')
SECRET_KEY = 'your_secret_key'
CERT_PATH = os.path.join(BASE_DIR, 'certs', 'cert.pem')
KEY_PATH = os.path.join(BASE_DIR, 'certs', 'key.pem')
