from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simples (lista)
alunos = [
    {
        "id": 1,
        "nome": "João",
        "idade": 17
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 16
    }
]

# Rota para listar todos os alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)



# Rota para buscar um aluno por ID
@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = next((a for a in alunos if a["id"] == id), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404



# Rota para adicionar um novo aluno
@app.route('/alunos', methods=['POST'])
def add_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201



# Rota para atualizar um aluno
@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    aluno = next((a for a in alunos if a["id"] == id), None)
    if aluno:
        dados = request.get_json()
        aluno.update(dados)
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404



# Rota para deletar um aluno
@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    global alunos
    alunos = [a for a in alunos if a["id"] != id]
    return jsonify({"mensagem": "Aluno removido com sucesso"})


# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)
