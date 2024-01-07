# Aula: Manipulando arquivos CSV em Python com Pacote CSV

'''
< CSV (Comma-Separated Values) é um formato de arquivo que armazena dados tabulares
em formato de texto plano. Cada linha do arquivo CSV representa uma linha da tabela
e as colunas são separadas por vírgulas. É amplamente utilizado para exportar e 
importar dados em diferentes aplicações, como planilhas e banco de dados. >
'''

# Importanto o módulo csv
import csv

CAMINHO_ARQUIVO = ".\\numeros.csv"

with open(CAMINHO_ARQUIVO, 'w') as arquivo:

    # Cria o objeto de gravação
    writer = csv.writer(arquivo)

    # Grava no arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3', 'nota4',))
    writer.writerow((63, 89, 92, 36))
    writer.writerow((61, 79, 76, 85))
    writer.writerow((72, 64, 91, 81))

# Leitura de arquivos CSV
with open(CAMINHO_ARQUIVO, 'r', encoding='utf8', newline='\r\n') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print(x)

print('-' * 75)

# Gerando uma lista com dados do arquivo csv:
with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)


print('-' * 75)

# Imprimindo a partir da segunda linha
for linha in dados[1:]:
    print(linha)
