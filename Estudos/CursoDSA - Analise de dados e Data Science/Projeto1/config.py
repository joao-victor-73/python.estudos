import menu
import random

''' REFERENCIA
\n\t[ 1 ] - FRUTAS
\t[ 2 ] - COMIDAS
\t[ 3 ] - CIDADES
\t[ 4 ] - ANIMAIS
\t[ 5 ] - ALEATÓRIOS
'''


def palavras_escolhida():
    categoria_palavra = menu.escolha_categoria()

    if categoria_palavra == 1:
        CAMINHO_ARQUIVO = ".\\Palavras\\frutas.txt"

    elif categoria_palavra == 2:
        CAMINHO_ARQUIVO = ".\\Palavras\\comidas.txt"

    elif categoria_palavra == 3:
        CAMINHO_ARQUIVO = ".\\Palavras\\cidades.txt"

    elif categoria_palavra == 4:
        CAMINHO_ARQUIVO = ".\\Palavras\\animais.txt"

    elif categoria_palavra == 5:
        CAMINHO_ARQUIVO = ".\\Palavras\\aleatorios.txt"

    with open(CAMINHO_ARQUIVO, 'r') as arq:
        palavras = arq.readlines()

    # Escolhe randomicamente uma palavra:
    palavra = random.choice(palavras)
    palavra = palavra.strip().upper()

    # Lista de letras da palavra
    lista_letras_palavras = [letra for letra in palavra]

    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)
