"""
                                        O QUE É JSON?
JSON(JavaScript Object Notation) é um formato baseado em chaves e valores, semelhante a um dicionário Python. 
Esse formato leve e amplamente utilizado para armazenar e transmitir dados entre sistemas, especialmente em APIs.

(em um breve resumo, um arquivo JSON nada mais é do que uma lista com dicionários)
Exemplo de um JSON:

{
  "nome": "João",
  "idade": 25,
  "cidade": "São Paulo",
  "habilidades": ["Python", "Flask", "SQL"]
}
"""

import json

# json.loads() -> Converte JSON(string) em dicionário Python
# json.loads() pega uma string JSON e transforma em um dicionário Python.

pessoa = '{"nome": "João", "idade": 25, "cidade": "São Paulo"}'

pessoa_dicionario = json.loads(pessoa)
print(pessoa_dicionario)
print(pessoa_dicionario['nome'])
print(type(pessoa_dicionario))


# json.dumps() -> Converte dicionário Python em JSON (string)
# json.dumps() retorna um JSON no formato string,
# pronto para ser enviado por uma API.

pessoa2 = {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"}
pessoa2_string = json.dumps(pessoa2)

print(pessoa2_string)
print(type(pessoa2_string))


# Escrever um JSON em um arquivo
# Podemos salvar um dicionário Python em um arquivo JSON usando json.dump():

pessoa3 = {"nome": "Carlos", "idade": 40, "cidade": "Brasília"}

with open("pessoa3.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa3, arquivo, indent=4)  # 'indent' deixa formatado (legível)


# Ler um JSON de um arquivo
# json.load() lê o conteúdo JSON do arquivo e o converte para um dicionário.

with open("pessoa3.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)
