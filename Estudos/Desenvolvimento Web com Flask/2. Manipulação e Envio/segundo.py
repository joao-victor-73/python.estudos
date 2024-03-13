# Primeiros passos e o básico para a introdução em Flask

from flask import Flask, render_template, request
# render_template é uma parte da biblioteca que serve para importar páginas HTML
# de uma pasta ou de algum lugar para a sua aplicação Flask

# O módulo <request> é o que nós permitirá requisitar ações no servidor. (aula10)

app = Flask(__name__)


nomes_pessoas = []
# Variável de uma lista sendo atribuida Globalmente (ou seja, fora da função principal);
# útil fazer assim quando o objetivo é alocar informações dentro de uma lista, dicionário, etc.


@app.route('/', methods=["GET", "POST"])  # edit na aula10
def principal():
    nome = "Paulo"
    idade = 22

    # Criando uma lista e colocando na página - Aula08: retornando valores da lista
    frutas = ['Morango', 'Abacaxi', 'Banana',
              'Maça', 'Laranja', 'Mamão', 'Limão']

    # Ve o tamanho(quantidade de itens) de uma lista.
    quantDeFrutas = len(frutas)

    # Criando um dicionário e colocando na página - Aula09: Retornando valores de dicionário
    preco_frutas = {'Morango': 5.87, 'Abacaxi': 2.40, 'Banana': 1.50,
                    'Maça': 1, 'Laranja': 2, 'Mamão': 2, 'Limão': 0.50}

    if request.method == "POST":
        if request.form.get("nomes"):
            nomes_pessoas.append(request.form.get("nomes"))

    return render_template("index2.html", nome=nome, idade=idade, frutas=frutas, quantDeFrutas=quantDeFrutas, preco_frutas=preco_frutas, nomes_pessoas=nomes_pessoas)


# feito na AULA 11
registros = []


@app.route('/sobre', methods=["GET", "POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            registros.append({"aluno": request.form.get(
                "aluno"), "nota": request.form.get("nota")})
    return render_template("sobre2.html", registros=registros)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
