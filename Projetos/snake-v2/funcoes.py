import pygame


def verifica_tecla(evento, cobra):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            cobra.direita = True


        if evento.key == pygame.K_LEFT:
            cobra.esquerda = True


def mudar_direcao():
    pass




'''

        # se uma tecla foi pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 cobra.muda_direcao('DIREITA')
            if event.key == pygame.K_UP:
                 cobra.muda_direcao('CIMA')
            if event.key == pygame.K_DOWN:
                 cobra.muda_direcao('BAIXO')
            if event.key == pygame.K_LEFT:
                 cobra.muda_direcao('ESQUERDA')
'''