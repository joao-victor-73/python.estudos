from flask import Flask, render_template, request

# Inicializações de variáveis
registros = []
lista_compras = []


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("descricao"):
            registros.append({"aluno": request.form.get("aluno"), "descricao": request.form.get("descricao")})
    return render_template("index3.html", registros=registros)


@app.route('/compras', methods=["GET", "POST"])
def compras():
    if request.method == "POST":
        if request.form.get("produto"):
            lista_compras.append(request.form.get("produto"))
    return render_template("compras.html", lista_compras=lista_compras)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
