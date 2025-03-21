import requests
from flask import Flask, jsonify

# requests → Usado para fazer requisições HTTP para APIs externas.
# Flask → Framework para criar a API.
# jsonify → Converte dados Python para JSON, o formato usado em APIs.


app = Flask(__name__)

API_KEY = 'c147135dcc6631cf191922bc5217dd97'  # "SUA_CHAVE_AQUI"
BASE_URL = "https://api.themoviedb.org/3"


@app.route('/filme/<titulo>', methods=['GET'])
def buscar_filme(titulo):

    # Esta função será executada sempre que alguém acessar a rota /filme/<titulo>.
    # O parâmetro titulo recebe o nome do filme passado na URL.

    url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={titulo}"
    resposta = requests.get(url) # Faz a requisição HTTP para o TMDB.
    dados = resposta.json() # Converte a resposta JSON em um dicionário Python.

    if "results" in dados and len(dados["results"]) > 0: # Verifica se há pelo menos um resultado
        return jsonify(dados["results"][0])  # Retorna o primeiro resultado
    else:
        return jsonify({"erro": "Filme não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
