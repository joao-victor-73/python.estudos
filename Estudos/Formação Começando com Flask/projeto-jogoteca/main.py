from flask import Flask, render_template, request, redirect


app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
