import pygame
import sys
from configs import Configuracoes
from cobra import Cobra
import funcoes as f

pygame.init()

configs = Configuracoes()

tela = pygame.display.set_mode((configs.tela_largura, configs.tela_altura))
pygame.display.set_caption("Jogo Cobra V.2")

while True:
    cobra = Cobra(configs, tela)

    tela.fill(configs.fundo_cor)  # Redesenha a tela a cada passagem do laço.

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()  # para o pygame
            sys.exit()  # fecha o script (janela)

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                cobra.posicao_y += 10
        

    cobrinha = cobra.desenha_cobra()
    pygame.display.update()
