import os

SECRET_KEY = 'alura'

# Fazendo a conexão com o banco de dados criando uma configuração no app
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:darc147@localhost/jogoteca'

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
