# import MySQLdb
import pymysql

"""
db_mysqldb = MySQLdb.connect(host='localhost',
                             user='root',
                             passwd='darc147',
                             db='jogoteca')"""



db_pymysql = pymysql.connect(host='localhost',
                             user='root',
                             passwd='darc147',
                             database='jogoteca')

cursor = db_pymysql.cursor()


# CONSULTA DOS REGISTROS JÁ ADICIONADOS
print("===================== JOGOS: =====================")
# Executando uma consulta SQL
cursor.execute("SELECT * FROM jogos")

# Recuperando todos os resultados da consulta
resultados = cursor.fetchall()

# Iterando sobre os resultados e imprimindo-os
for linha in resultados:
    print(linha)
