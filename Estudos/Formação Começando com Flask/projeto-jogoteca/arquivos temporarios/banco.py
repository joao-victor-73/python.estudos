import pymysql

"""
Lembrar que os comandos abaixo só irão funcionar caso
a 'database' do mini-projeto esteja criado.

Também tem que criar as tabelas 'Jogos' e 'Usuários';

Depois adicionar já alguns registros;
"""

# CONECTANDO AO BANCO DE DADOS
db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='darc147',
    database='jogoteca')


# ------------------------------------------------------------------

# EXECUTAR CONSULTAS / FAZER CONSULTAS
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

# criando uma consulta SQL
sql = "SELECT * FROM teste1"

# Executando a consulta
cursor.execute(sql)

# Pega todos os resultados da consulta
result = cursor.fetchall()
    
# Imprime os resultados
for linha in result:
    print(linha)
    
# Fecha a conexão com o banco de dados
db.close()

# ------------------------------------------------------------------

# INSERÇÃO DE DADOS

# Define a consulta de inserção
sql = "INSERT INTO sua_tabela (coluna1, coluna2) VALUES (%s, %s)"

# Executa a inserção com os valores
cursor.execute(sql, ('valor1', 'valor2'))

# Confirma a transação
db.commit()

# ------------------------------------------------------------------

"""
O que é a Variável 'sql'?
    - A variável sql é uma string em Python que contém um comando SQL. 
      Esse comando pode ser qualquer tipo de instrução SQL, 
      como: SELECT, INSERT, UPDATE, DELETE, ou comandos mais avançados, 
      dependendo do que você deseja fazer no banco de dados.
"""