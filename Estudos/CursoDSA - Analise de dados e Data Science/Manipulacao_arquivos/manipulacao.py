

# Abrindo o arquivo para leitura
CAMINHO_ARQUIVO = "C:\\Users\\jvt86\\OneDrive\\Documentos\\MeusProjetos\\Pyhton\\Estudos\\CursoDSA - Analise de dados e Data Science\\Manipulacao_arquivos\\arquivo_teste.txt"
CAMINHO_ARQUIVO2 = "C:\\Users\\jvt86\\OneDrive\\Documentos\\MeusProjetos\\Pyhton\\Estudos\\CursoDSA - Analise de dados e Data Science\\Manipulacao_arquivos\\arquivo_teste2.txt"
CAMINHO_ARQUIVO3 = "C:\\Users\\jvt86\\OneDrive\\Documentos\\MeusProjetos\\Pyhton\\Estudos\\CursoDSA - Analise de dados e Data Science\\Manipulacao_arquivos\\salarios.csv"

arquivo1 = open(CAMINHO_ARQUIVO, "r")  # r = read
# print(type(arquivo1))

# Lendo o arquivo
print(arquivo1.read())

# Abrindo o Arquivo para gravação
arquivo2 = open(CAMINHO_ARQUIVO2, "w")  # w = write
# (Caso o arquivo não exista, ele criará, mas caso ele já esteja criado, ele sobrescreverá)

# Escrevendo no arquivo:
arquivo2.write("ADICIONANDO MAIS UMA LINHA AO SEGUNDO ARQUIVO DE TEXTE.TXT")
arquivo2.close()

# Acrescentando conteúdo ao final
arquivo2 = open(CAMINHO_ARQUIVO2, "a")  # a = append
arquivo2.write(" E a metodologia de ensino!")


print('-' * 50)

# Manipulando arquivos com o Pacote PANDAS
import pandas as pd

arquivo3 = CAMINHO_ARQUIVO3
df = pd.read_csv(arquivo3)
df.head()

