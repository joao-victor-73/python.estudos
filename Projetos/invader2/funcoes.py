import sys
import pygame


def press_tecla(evento, nave):
    # Responde a pressionamento de tecla
    if evento.key == pygame.K_RIGHT:
        # Move a espaçonave para a direita
        nave.mover_direita = True  # vai fazer efeito na def atualizar na classe nave

    elif evento.key == pygame.K_LEFT:
        nave.mover_esquerda = True


def soltar_teca(evento, nave):
    # Responde quando soltar uma tecla
    if evento.key == pygame.K_RIGHT:
        nave.mover_direita = False

    elif evento.key == pygame.K_LEFT:
        nave.mover_esquerda = False


def checar_eventos(nave):
    # Responde a eventos de pressionamento de teclas e de mouse
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            press_tecla(evento, nave)

        elif evento.type == pygame.KEYUP:
            soltar_teca(evento, nave)


def atualizacao_tela(configs, tela, nave):
    # Os nomes dos parâmetros são os mesmos para falicitar!
    tela.fill(configs.fundo_tela)

    nave.blitme()  # Faz a nave aparecer na tela

    pygame.display.flip()  # Deixa a tela recente vísivel.
