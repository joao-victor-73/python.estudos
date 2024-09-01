# import MySQLdb
import pymysql

"""
Lembrar que os comandos abaixo só irão funcionar caso
a 'database' do mini-projeto esteja criado.

Também tem que criar as tabelas 'Jogos' e 'Usuários';

Depois adicionar já alguns registros;
"""

# ------------------------------------------------------------------

# CONECTANDO AO BANCO DE DADOS
db = pymysql.connect(host='localhost',
                     user='root',
                     passwd='darc147',
                     database='jogoteca')


"""
O QUE É UM CURSOR?
    - Definição: Um cursor é um objeto que permite a execução de consultas SQL e 
                fornece uma maneira de acessar linha a linha os resultados retornados 
                por uma consulta.
    
    - Função: Ele é usado para enviar comandos SQL ao banco de dados e para iterar sobre 
              os resultados retornados por essas consultas. Pense no cursor como um 
              ponteiro ou uma referência a um contexto de execução de banco de dados 
              que mantém o estado da operação atual.
"""

cursor = db.cursor()

# ------------------------------------------------------------------

# CRIANDO AS TABELAS
SQL_CRIA_TABELA_JOGOS = """ CREATE TABLE IF NOT EXISTS jogos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    login_user VARCHAR(100) NOT NULL,
    senha_user VARCHAR(100) NOT NULL
);"""

SQL_CRIA_TABELA_USUARIOS = """ CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    console VARCHAR(100) NOT NULL
);"""


# EXECUTANDO OS COMANDOS DE CRIAÇÃO
cursor.execute(SQL_CRIA_TABELA_JOGOS)
cursor.execute(SQL_CRIA_TABELA_USUARIOS)

print("========== TABELAS CRIADAS COM SUCESSO ==========")

# ------------------------------------------------------------------

# ADICIONANDO REGISTRO AS TABELAS

# Definindo o comando SQL para inserir múltiplos registros
SQL_INSERIR_JOGOS = """
INSERT INTO jogos (nome, categoria, console)
VALUES (%s, %s, %s)
"""

# Lista de múltiplos jogos para serem inseridos
jogos = [
    ('God of War 2', 'Ação', 'PS3'),
    ('Devil May Cry 4', 'Rogue Like', 'PS4'),
    ('Minecraft', 'Aventura', 'PC')
]


""" <PARA ADICIONAR UM ÚNICO REGISTRO>
SQL_INSERIR_JOGO = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogo = ("Pokemon Arceus", "Aventura", "Nintendo Switch")

cursor.execute(SQL_INSERIR_JOGO, jogo)
"""


# Executando o comando SQL para cada registro de jogo
cursor.executemany(SQL_INSERIR_JOGOS, jogos)

# ------------------------------------------------------------------


# CONSULTA DOS REGISTROS JÁ ADICIONADOS
SQL_CONSULTA_JOGOS = "SELECT * FROM jogos;"
SQL_CONSULTA_USUARIOS = "SELECT * FROM usuarios;"


print("===================== JOGOS: =====================")
# Executando uma consulta SQL
cursor.execute(SQL_CONSULTA_JOGOS)

# Recuperando todos os resultados da consulta
resultados = cursor.fetchall()

# Iterando sobre os resultados e imprimindo-os
for jogo in resultados:
    print(jogo)

print("# ------------------------------------------------------------------ #")

print("===================== USUARIOS: =====================")
# Executando uma consulta SQL
cursor.execute(SQL_CONSULTA_JOGOS)

# Recuperando todos os resultados da consulta
resultados = cursor.fetchall()

# Iterando sobre os resultados e imprimindo-os
for user in resultados:
    print(user)


# ------------------------------------------------------------------


# CONFIRMANDO A TRANSAÇÃO
db.commit()

# FECHANDO O BANDO DE DADOS APÓS OS COMANDOS
db.close()
