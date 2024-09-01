from flask import Flask, render_template, request, redirect, session, flash, url_for
# from flask_mysqldb import MySQL
from models import Jogo, Usuario
from dao import JogoDao
import pymysql


app = Flask(__name__)
app.secret_key = 'caelum'
# é uma chave secreta para o session, pode ser qualquer informação dentro da string

# Configurações do banco de dados
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'darc147'
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_PORT'] = 3306


# Configuração da conexão com PyMySQL
def get_db_connection():
    connection = pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT'],
        cursorclass=pymysql.cursors.DictCursor
    )

    """
    A função get_db_connection() encapsula a criação da conexão 
    para facilitar o uso em diferentes partes do seu aplicativo

    Usamos `pymysql.cursors.DictCursor` para que os resultados da 
    consulta sejam retornados como dicionários, o que é conveniente 
    para acessar os resultados pelos nomes das colunas.
    """

    return connection


db = get_db_connection()

jogo_dao = JogoDao(db)


jogo1 = Jogo("Mario Bros 3", "Plataforma", "SNES")
jogo2 = Jogo("Contra 4", "Ação", "PS2")
jogo3 = Jogo("Devil May Cry", "Rogue Like", "Ação")
lista = [jogo1, jogo2, jogo3]

user1 = Usuario('luan', 'Luan Marques', '1234')
user2 = Usuario('vitor', 'Vitor Lima', '4321')
usuarios = {user1.id: user1, user2.id: user2}


@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista)


@app.route('/novo')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima_pagina=url_for('novo_jogo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar_jogo():
    nome_jogo = request.form.get('nome', False)
    categoria_jogo = request.form.get('categoria', False)
    console_jogo = request.form.get('console', False)

    # Instânciando a classe Jogo com as informações do formulário do HTML
    jogo = Jogo(nome_jogo, categoria_jogo, console_jogo)

    # Adicionando as informações da classe Jogo na lista
    jogo_dao.salvar(jogo)

    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima_pagina')
    return render_template('login.html', proxima_pagina=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:

        user = usuarios[request.form['usuario']]

        if user.senha == request.form['senha']:

            session['usuario_logado'] = user.id
            flash(f'{user.nome} logou com sucesso!')

            proxima_pagina_apos_login = request.form['proxima_pagina']

            return redirect(proxima_pagina_apos_login)

    else:
        flash('Não foi possível efetuar o login!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
