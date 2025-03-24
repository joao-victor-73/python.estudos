# PyMySQL - Um cliente MySQL feito em Python Puro

import pymysql
import dotenv
import os


# Importar informações de um arquivo .env que está dentro da mesma pasta desse arquivo 'main.py'
dotenv.load_dotenv()


# Conectar ao MySQL e abrir a conexão
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)


cursor = connection.cursor()


# SQL COMANDS
cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers ( '
    'id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, '
    'nome VARCHAR(50) NOT NULL, '
    'idade INT NOT NULL '
    ') '
)

# CUIDADO: Esse comando faz a limpeza na tabela, ou seja, apaga tudo.
cursor.execute('TRUNCATE TABLE customers')
connection.commit()


# Manipular dados:

# Inserindo um valor usando placeholder e um iterável
sql_insert = (
    'INSERT INTO customers (nome, idade) VALUES '
    '(%s, %s) '
)
cursor.execute(sql_insert, ('Luiz', 18))
connection.commit()


# Inserindo dados através de placeholder e dicionário
sql_insert_2 = (
    'INSERT INTO customers (nome, idade) VALUES '
    '(%(name)s, %(age)s) '
)
dados = {
    "name": "Le",
    "age": 27
}
cursor.execute(sql_insert_2, dados)
connection.commit()


# Inserindo vários valores usando placeholder e uma tupla de dicionários
sql_insert_3 = (
    'INSERT INTO customers (nome, idade) VALUES '
    '(%(name)s, %(age)s) '
)

dados2 = (  # Isso é um iterável de dicionários (ou uma tupla de dicionários)
    {"name": "Sah", "age": 33},
    {"name": "Julia", "age": 74},
    {"name": "Rose", "age": 53}
)

cursor.executemany(sql_insert_3, dados2)
connection.commit()


# Lendo os valores com SELECT
sql_select = (
    'SELECT * FROM customers '
)

cursor.execute(sql_select)
dados3 = cursor.fetchall()

# Percorrendo os registros coletados do fetchall()
for row in dados3:
    print(row)


print()

# DELETANDO VALORES da tabela:
sql_delete = (
    'DELETE FROM customers ' \
    'WHERE id = %s '
)
cursor.execute(sql_delete, (4, ))
connection.commit()

cursor.execute(sql_select)
dados_pos_delete = cursor.fetchall()

for row in dados_pos_delete:
    print(row)


print()



# Editando registros da tabela:
sql_update = (
    'UPDATE customers ' \
    'SET idade = 40 ' \
    'WHERE id = %s ' 
)
cursor.execute(sql_update, (2, ))
connection.commit()

cursor.execute(sql_select)
dados4 = cursor.fetchall()

for row in dados4:
    print(row)


# Fechar uma conexão
connection.close()
