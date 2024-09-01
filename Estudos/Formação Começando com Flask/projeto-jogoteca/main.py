from flask import Flask, render_template, request, redirect, session, flash, url_for
# from flask_mysqldb import MySQL
from models import Jogo, Usuario
from dao import JogoDao, UsuarioDao
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
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
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
    login_user = request.form.get('usuario', '')
    senha_user = request.form.get('senha', '')

    print(f"Login: {login_user}, Senha: {senha_user}")

    user = usuario_dao.buscar_por_id(login_user)
    # Isso é para retornar o usuário que foi digitado no forms de login
    print(f"Usuário encontrado: {user}")

    if user:
        if user.senha_user == senha_user:
            session['usuario_logado'] = user.id
            flash(f'{user.nome} logou com sucesso!')

            proxima_pagina_apos_login = request.form.get(
                'proxima_pagina', url_for('index'))

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
