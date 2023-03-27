import sys
import pygame
from settings import Configurações
from nave import Nave
import funcoes as f

configs = Configurações()  # ai_settings = configs


def rodando_jogo():
    # Função que rodará o jogo!

    pygame.init()  # -> Faz a inicialização de todo o jogo!

    tela = pygame.display.set_mode((configs.tela_largura, configs.tela_altura))
    pygame.display.set_caption("JOGUINHO!")

    # Trazendo as informações da nave para o programa principal!
    nave = Nave(tela, configs)

    while True:  # Laço principal de todo o jogo!
        f.checar_eventos(nave)

        nave.atualizar()

        f.atualizacao_tela(configs, tela, nave)


rodando_jogo()
