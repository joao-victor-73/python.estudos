import pygame.font


class Scoreboard():
    '''< Uma classe para mostrar informações sobre pontuação. >'''

    def __init__(self, configs, tela, stats):
        '''< Inicializa os atributos da pontuação. >'''
        self.tela = tela
        self.tela_rect = tela.get_rect()
        self.configs = configs
        self.stats = stats

        # Configurações de fonte para as informações de pontuação
        self.cor_texto = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepara a imagem da pontuação inicial
        self.prep_score()

    def prep_score(self):
        '''< Transforma a pontuação em uma imagem renderizada. >'''
        score_str = str(self.stats.pontuacao)
        self.pontuacao_imagem = self.font.render(
            score_str, True, self.cor_texto, self.configs.fundo_tela)

        # Exibe a pontuação na parte superior direita da tela
        self.pontuacao_rect = self.pontuacao_imagem.get_rect()
        self.pontuacao_rect.right = self.tela_rect.right - 20
        self.pontuacao_rect.top = 20

    def mostrar_pontuacao(self):
        '''< Desenha a pontuação na tela. >'''
        self.tela.blit(self.pontuacao_imagem, self.pontuacao_rect)
