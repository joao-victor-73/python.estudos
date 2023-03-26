import pygame
from configs import Configurações

config = Configurações()


def fontes(fonte='arial', tamanho=15, negrito=False, italico=False):
    # Fonte = o tipo de fonte que vai querer;
    # tamanho = O tamanho da Fonte (valores inteiros);
    # Negrito = Colocar True para colocar em negrito
    # Italico = Colocar True para colocar em Italico

    return pygame.font.SysFont(fonte, tamanho, negrito, italico)


def mensagem_pontos():
    m = fontes('arial', 25)
    mensagem = f'Pontos: {config.pontos}'
    texto_formatado = m.render(mensagem, False, (255, 255, 255))

    return texto_formatado


def mensagem_game_over():
    """
    Função mensagem_game_over vai retornar dois valores: texto_retangulo e texto_formatado
    Dentro do looping de reiniciar preciso, para atualizar a tela, da variável
    texto_formatado.
    """

    fonte = fontes('Arial', 15, True, True)
    texto = 'Game Over! Pressione "R" para jogar novamente!'
    texto_formatado = fonte.render(texto, True, (0, 0, 0))

    texto_retangulo = texto_formatado.get_rect()

    return texto_formatado, texto_retangulo
