import pygame


class Mensagens():
    def __init__(self, config, msg, tela, cor):
        self.tela = tela
        self.tela_rect = tela.get_rect()

        self.config = config

        # Mensagem de Game Over quando morrer.
        self.msg = msg

        self.cor = cor

        # Configuracoes para o texto
        self.cor_texto = self.cor.indigo
        self.fonte = pygame.font.SysFont('arial', 15, True, True)

        self.prep_mensagem()

    def prep_mensagem(self):
        '''< Transforma a mensagem em uma imagem renderizada. >'''
        self.men_over = self.fonte.render(self.msg, True, self.cor.preto)

        self.men_over_rect = self.men_over.get_rect()

        # Exibe a mensagem no meio da tela
        self.men_over_rect.center = (
            self.config.tela_largura // 2, self.config.tela_altura // 2)

    def monstrar_mensagem(self):
        self.tela.blit(self.men_over, self.men_over_rect)


''''
def fontes(fonte='arial', tamanho=15, negrito=False, italico=False):
    # Fonte = o tipo de fonte que vai querer;
    # tamanho = O tamanho da Fonte (valores inteiros);
    # Negrito = Colocar True para colocar em negrito
    # Italico = Colocar True para colocar em Italico

    return pygame.font.SysFont(fonte, tamanho, negrito, italico)


def mensagem_pontos(pontos):
    m = fontes('arial', 25)
    mensagem = f'Pontos: {pontos}'
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
'''
