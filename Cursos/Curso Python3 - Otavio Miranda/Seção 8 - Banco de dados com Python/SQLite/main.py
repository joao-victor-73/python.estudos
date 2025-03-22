import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

# Comando para criar ou conectar ao banco de dados
# (Cria um arquivo, que nesse caso o nome do arquivo está
# na variável (DB_FILE), se não existir)
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# COMANDOS SQL

# Criando tabelas
cursor.execute(
    'CREATE TABLE IF NOT EXISTS customers'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

# Salvando alterações
connection.commit()


# Inserindo registros na tabela
sql = (
    'INSERT INTO customers (name, weight) '
    'VALUES (?, ?)'
)
cursor.execute(sql, ['Caio Henrique', 9.9])
connection.commit()

# Inserindo vários registros na tabela
# Pode ser tupla ou listas, para o comando executemany não importa.
cursor.executemany(sql, [['Joana', 9], ['Fernando', 4], ['Otavio', 34]])
connection.commit()


# Fazendo uma Consulta
cursor.execute('SELECT * FROM customers')

# fetchall() -> retorna todos os valores da tabela
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

# fecthone() -> trás apenas o primeiro registro da consulta
row_one = cursor.fetchone()
print(row_one)


# Deletando no SQLite
# CUIDADO ao fazer um DELETE sem WHERE

# DELETE correto:
cursor.execute(
    'DELETE FROM customers WHERE id = 1'
)
connection.commit()


# Atualizando registros na tabela
cursor.execute(
    'UPDATE customers '
    'SET name = "Paulo" '
    'WHERE id = 1'
)


# Fechar a conexão
cursor.close()
connection.close()


if __name__ == "__main__":
    cursor.close()
    connection.close()
