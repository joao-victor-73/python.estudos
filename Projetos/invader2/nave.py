import pygame

'''
tela_retangulo = screen_rect
self.retangulo = self.rect
moving_right = mover_direita
moving_left = mover_esquerda
'''


class Nave():
    def __init__(self, tela, configs):
        self.tela = tela
        self.configs = configs

        self.imagem = pygame.image.load(
            'Projetos\\invader2\\imagens\\nave2.bmp')
        self.imagem = pygame.transform.scale(self.imagem, [80, 80])
        self.rect = self.imagem.get_rect()
        # vai transformar a imagem acima em um retângulo!

        self.tela_retangulo = tela.get_rect()

        self.rect.centerx = self.tela_retangulo.centerx
        # vai pegar o valor do centro de X da tela e dizer que vai ser a mesma que a imagem!

        self.rect.bottom = self.tela_retangulo.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.centro = float(self.rect.centerx)

        # Flags de Movimentação
        self.mover_direita = False
        self.mover_esquerda = False

    def atualizar(self):
        # Atualiza a posição da espaçonave de acordo com as flags de movimento!

        # Vai fazer a movimentação bloquear nos limites da tela
        if self.mover_direita and self.rect.right < self.tela_retangulo.right:
            self.centro += self.configs.nave_velocidade

        if self.mover_esquerda and self.rect.left > 0:
            self.centro -= self.configs.nave_velocidade

        # Atualiza o objeto retangulo de acordo com self.center
        self.rect.centerx = self.centro

    def blitme(self):
        # Desenha a espaçonave em sua posição atual
        self.tela.blit(self.imagem, self.rect)

    def centro_nave(self):
        ''' Centraliza a espaçonave na tela! '''
        self.center = self.tela_retangulo.centerx