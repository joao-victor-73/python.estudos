# Projeto 1 - Desenvolvimento de Game em Python - Aula 1/5

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
