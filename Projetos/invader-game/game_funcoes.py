import sys
import pygame


def adm_events(nave):
    """
    Essa função responde a eventos de pressionamento de teclas e de mouse.
    """
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                # Se tiver precionado, vai se tornar True.
                nave.movendo_direita = True

            elif evento.key == pygame.K_LEFT:
                nave.movendo_esquerda = True

        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                # Se parar de presionar, vai se tornar False.
                nave.movendo_direita = False

            elif evento.key == pygame.K_LEFT:
                nave.movendo_esquerda = False


def att_tela(config, tela, nave):  # config == ai_settings / att_tela == update screen
    """
    Atualiza as imagens na tela e alterna para a nova tela.
    """
    tela.fill(config.fundo_cor)  # fundo_cor == bg_color
    nave.blitme()

    pygame.display.flip()  # Deixa a tela mais recente visível
