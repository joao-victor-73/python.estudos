from flask import Flask, render_template, request

# Inicializações de variáveis
registros = []
lista_compras = []
lista_preco = []
lista_produtos = []


app = Flask(__name__)


class Produtos:
    def __init__(self, id, nomeProduto, precoProduto, dataCompra, ondeCompra):
        self.id = id
        self.nomeProduto = nomeProduto
        self.precoProduto = precoProduto
        self.dataCompra = dataCompra
        self.ondeCompra = ondeCompra


@app.route('/', methods=["GET", "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("descricao"):
            registros.append({"aluno": request.form.get(
                "aluno"), "descricao": request.form.get("descricao")})
    return render_template("index5.html", registros=registros)


@app.route('/compras', methods=["GET", "POST"])
def compras():
    if request.method == "POST":
        if request.form.get("produto"):
            lista_compras.append(request.form.get("produto"))

    return render_template("compras.html", lista_compras=lista_compras)


@app.route('/produtos', methods=["GET", "POST"])
def produtos():
    if request.method == "POST":
        # Variáveis para requisição
        nome_p = request.form.get("nome_produto")
        preco_p = request.form.get("preco_produto")
        data_p = request.form.get("data_compras")
        onde_p = request.form.get("onde_comprar")
        id_p = len(lista_produtos) + 1

        if nome_p and preco_p and data_p and onde_p:
            novo_produto = Produtos(id_p, nome_p, preco_p, data_p, onde_p)
            lista_compras.append(novo_produto)

            print("Nome do produto:", nome_p)
            print("Preço do produto:", preco_p)
            print("Data das compras:", data_p)
            print("Onde comprar:", onde_p)

            # Verificando se a lista está sendo populada corretamente
            print("Lista de produtos:", lista_produtos)

    return render_template("list_compras.html", lista_produtos=lista_produtos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
