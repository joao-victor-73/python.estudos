import pygame
import sys

def press_teclas(evento, x_controle, y_controle, config):
    if evento.key == pygame.K_LEFT:
        if x_controle == config.velocidade:
                pass
        else:
            x_controle = -config.velocidade
            y_controle = 0

        if evento.key == pygame.K_RIGHT:
            if x_controle == -config.velocidade:
                pass
            else:
                x_controle = config.velocidade
                y_controle = 0

        if evento.key == pygame.K_UP:
            if y_controle == config.velocidade:
                pass
            else:
                y_controle = -config.velocidade
                x_controle = 0

        if evento.key == pygame.K_DOWN:
            if y_controle == -config.velocidade:
                pass
            else:
                y_controle = config.velocidade
                x_controle = 0


def check_eventos(x_controle, y_controle, config):
        # o lopping for vai servir para checar os eventos!
    for evento in pygame.event.get():
        # Vai servir para poder fechar a janela
        if evento.type == pygame.QUIT:
            sys.exit()

        # Vai fazer com que a cobra fique em constante movimento.
        if evento.type == pygame.KEYDOWN:
            press_teclas(evento, x_controle, y_controle, config)
