# Projeto 1 - Desenvolvimento de Game em Python - Aula 3/5

# Importando bibliotecas
import random
from os import system, name


def limpa_tela():
    '''Função para limpar a tela a cada execução.'''

    # Se for Windows:
    if name == 'nt':
        _ = system('cls')

    # Se for outro sistema (Mac ou Linux):
    else:
        _ = system('clear')


def game():

    limpa_tela()

    print("\nBem-vindo(a) ao >>JOGO DA FORCA<<")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolhe randomicamente uma palavra:
    palavra = random.choice(palavras)

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero:
    while chances > 0:

        print(" ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0
            
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
