# Aula: Manipulando Arquivos JSON em Python com Pacote JSON

'''
< JSON (JavaScript Object Notation) é um formato de dados de texto simples e leve
que é utilizado para trasmitir informações em aplicações web. É baseado em uma 
estrutura de objetos JavaScript e usa pares de chave-valor para representar dados. >
'''

# Importando o módulo JSON
import json

# Criando um dicionário
dict_guido = {'Nome': 'Guido Van Rossum',
              'Linguagem': 'Python',
              'Similar': ['C', 'Modula-J', 'lisp'],
              'Users': 226523}

for k, v in dict_guido.items():
    print(k, v)

# Convertendo o dicionário para um objeto json
json.dumps(dict_guido)

# Criando um arquivo json
ARQUIVO_JSON = '.\\dados.json'
with open(ARQUIVO_JSON, 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

# Leitura de arquivos Json
with open(ARQUIVO_JSON, 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

dados

print(dados['Nome'])
