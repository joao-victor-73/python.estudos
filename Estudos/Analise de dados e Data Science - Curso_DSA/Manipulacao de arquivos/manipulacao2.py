# Aula: Manipulando Arquivos TXT em Python com o Pacote OS

# Importando pacote OS
import os

# Criarei três frases
texto = "Isso é um texto que diz uma frase que vai fazer sentido em algum momento. \n"
texto = texto + "Vamos colocar essa frase concatenada com a anterior. \n"
texto += "E é claro, devemos adicionar uma linha final. -----------------"

# print(texto)

# Criando uma variável p/ receber o caminho da pasta
CAMINHO_RAIZ = os.path.join('texto3.txt')

# Criando um arquivo:
arquivo = open(CAMINHO_RAIZ, 'w')

# Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

# Fechando o arquivo
arquivo.close()

# Lendo o arquivo
arquivo = open(CAMINHO_RAIZ, 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
