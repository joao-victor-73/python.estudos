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
            'Projetos\\invader2\\imagens\\nave_galata.bmp')
        self.imagem = pygame.transform.scale(self.imagem, [80, 80])
        self.retangulo = self.imagem.get_rect()
        # vai transformar a imagem acima em um retângulo!

        self.tela_retangulo = tela.get_rect()

        self.retangulo.centerx = self.tela_retangulo.centerx
        # vai pegar o valor do centro de X da tela e dizer que vai ser a mesma que a imagem!

        self.retangulo.bottom = self.tela_retangulo.bottom

        # Armazena um valor decimal para o centro da espaçonave
        self.centro = float(self.retangulo.centerx)

        # Flags de Movimentação
        self.mover_direita = False
        self.mover_esquerda = False

    def atualizar(self):
        # Atualiza a posição da espaçonave de acordo com as flags de movimento!

        # Vai fazer a movimentação bloquear nos limites da tela
        if self.mover_direita and self.retangulo.right < self.tela_retangulo.right:
            self.centro += self.configs.nave_velocidade

        if self.mover_esquerda and self.retangulo.left > 0:
            self.centro -= self.configs.nave_velocidade

        # Atualiza o objeto retangulo de acordo com self.center
        self.retangulo.centerx = self.centro

    def blitme(self):
        # Desenha a espaçonave em sua posição atual
        self.tela.blit(self.imagem, self.retangulo)
