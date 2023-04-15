import pygame
import sys


def colisoes_maca(config, comida, musicas, cobrinha, maca):
    if cobrinha.colliderect(maca):
        comida.maca_x = comida.maca_x
        comida.maca_y = comida.maca_y
        # cada vez que o retangulo 1 colider com o outro, os valores X e Y serão
        # randimicamentes alterados

        config.pontos += 1  # toda vez que houver colisão, os pontos vão subir

        config.comprimento_inicial += 1

        # Coisa extra: toda vez que coletar 10 pontos, ele toca uma outra música
        config.cont += 1
        if config.cont == 10:
            musicas.musica_10pontos.play()
            config.cont = 0
        else:
            # O barulho de colisão apenas rodará quando ouver colisão
            musicas.musica_coleta.play()

    # Vai deixar o jogo mais rapido quando atingir determinado x pontos
    if config.pontos >= 20:
        config.velocidade = 20
