# Aula sobre o CSV - Comma Separated Values

import csv  # Importando módulo para usar as funções csv
from pathlib import Path  # Biblioteca que serve para caminhos de arquivos

CAMINHO_CSV = Path(__file__).parent / 'aula292_csv.csv'
# Vai servir apenas para pegar o caminho do arquivo citado entre '...'.

# Utilizando a função csv.reader para leitura
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)

print('=' * 27)

# Utilizando a função csv.DictReader para leitura como dicionário
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
