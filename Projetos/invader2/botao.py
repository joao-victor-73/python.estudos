import pygame.font


class Botao():
    def __init__(self, configs, tela, msg):
        ''' Inicializa os atributos do botão. '''
        self.tela = tela
        self.tela_rect = tela.get_rect()

        # Define as dimensões e as propriedades do botão
        self.largura, self.altura = 200, 50
        self.botao_cor = (0, 255, 0)
        self.cor_texto = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Constrói o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.largura, self.altura)
        self.rect.center = self.tela_rect.center

        # A mensagem do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        ''' Transforma msg em imagem renderizada e centraliza o texto no botão. '''
        self.msg_imagem = self.font.render(
            msg, True, self.cor_texto, self.botao_cor)
        
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.center = self.rect.center

    def desenhar_botao(self):
        # Desenha um botão em branco e, em seguida, desenha a mensagem
        self.tela.fill(self.botao_cor, self.rect)
        self.tela.blit(self.msg_imagem, self.msg_imagem_rect)
