from flask import Flask, render_template, request, redirect, session, flash


app = Flask(__name__)
app.secret_key = 'caelum'
# é uma chave secreta para o session, pode ser qualquer informação dentro da string


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("Mario Bros 3", "Plataforma", "SNES")
jogo2 = Jogo("Contra 4", "Ação", "PS2")
jogo3 = Jogo("Devil May Cry", "Rogue Like", "Ação")
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def inicio():
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista)


@app.route('/novo')
def novo_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar_jogo():
    nome_jogo = request.form.get('nome', False)
    categoria_jogo = request.form.get('categoria', False)
    console_jogo = request.form.get('console', False)

    # Instânciando a classe Jogo com as informações do formulário do HTML
    jogo = Jogo(nome_jogo, categoria_jogo, console_jogo)

    # Adicionando as informações da classe Jogo na lista
    lista.append(jogo)

    return redirect('/')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'{request.form['usuario']} logou com sucesso!')
        return redirect('/')
    else:
        flash('Não foi possível efetuar o login!')
        return redirect('/login')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
