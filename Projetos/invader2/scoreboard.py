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
        self.prep_max_pontuacao()
        self.prep_level()

    def prep_score(self):
        '''< Transforma a pontuação em uma imagem renderizada. >'''
        arredondar_pontuacao = int(round(self.stats.pontuacao, -1))
        score_str = "{:,}".format(arredondar_pontuacao)
        self.pontuacao_imagem = self.font.render(
            score_str, True, self.cor_texto, self.configs.fundo_tela)

        # Exibe a pontuação na parte superior direita da tela
        self.pontuacao_rect = self.pontuacao_imagem.get_rect()
        self.pontuacao_rect.right = self.tela_rect.right - 20
        self.pontuacao_rect.top = 20

    def prep_max_pontuacao(self):
        '''< Transforma a pontuação máxima em uma imagem renderizada. >'''
        max_pontuacao = int(round(self.stats.max_pontuacao, -1))
        max_pontuacao_str = "{:,}".format(max_pontuacao)
        self.max_pontuacao_imagem = self.font.render(
            max_pontuacao_str, True, self.cor_texto, self.configs.fundo_tela)

        # Centraliza a pontuaçãoa máxima na parte superior da tela
        self.max_pontuacao_rect = self.max_pontuacao_imagem.get_rect()
        self.max_pontuacao_rect.centerx = self.tela_rect.centerx
        self.max_pontuacao_rect.top = self.pontuacao_rect.top

    def prep_level(self):
        '''< Transforma o nível em uma imagem renderizada. >'''
        self.level_imagem = self.font.render(
            str(self.stats.level), True, self.cor_texto, self.configs.fundo_tela)

        # Posiciona o nível abaixo da pontuação
        self.level_rect = self.level_imagem.get_rect()
        self.level_rect.right = self.pontuacao_rect.right
        self.level_rect.top = self.pontuacao_rect.bottom + 10

    def mostrar_pontuacao(self):
        '''< Desenha a pontuação na tela. >'''
        self.tela.blit(self.pontuacao_imagem, self.pontuacao_rect)
        self.tela.blit(self.max_pontuacao_imagem, self.max_pontuacao_rect)
        self.tela.blit(self.level_imagem, self.level_rect)
