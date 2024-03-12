# Primeiros passos e o básico para a introdução em Flask

from flask import Flask, render_template
# render_template é uma parte da biblioteca que serve para importar páginas HTML
# de uma pasta ou de algum lugar para a sua aplicação Flask

app = Flask(__name__)


@app.route('/')
def principal():
    return render_template("index.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
