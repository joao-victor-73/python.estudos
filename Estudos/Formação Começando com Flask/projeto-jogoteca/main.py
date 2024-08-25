from flask import Flask, render_template, request


app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/')
def inicio():
    jogo1 = Jogo("Mario Bros 3", "Plataforma", "SNES")
    jogo2 = Jogo("Contra 4", "Ação", "PS2")
    jogo3 = Jogo("Devil May Cry", "Rogue Like", "Ação")
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', lista_jogos=lista)


@app.route('/novo')
def novo_jogo():
    return render_template('novo.html', titulo='Novo Jogo')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
