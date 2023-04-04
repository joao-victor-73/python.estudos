import sys
import pygame
from pygame.sprite import Group
from settings import Configurações
from nave import Nave
from alien import Alien
import funcoes as f

configs = Configurações()  # ai_settings = configs


def rodando_jogo():
    # Função que rodará o jogo!

    pygame.init()  # -> Faz a inicialização de todo o jogo!

    tela = pygame.display.set_mode((configs.tela_largura, configs.tela_altura))
    pygame.display.set_caption("JOGUINHO!")

    # Trazendo as informações da nave para o programa principal!
    nave = Nave(tela, configs)

    projeteis = Group()  # Cria um grupo no qual serão armazenados os projéteis!

    aliens = Group()  # Cria um grupo para armazenar a frota de alienigena

    f.criar_frota(configs, tela, nave, aliens)  # Cria uma frota de alienígena.

    while True:  # Laço principal de todo o jogo!
        f.checar_eventos(configs, tela, nave, projeteis)

        nave.atualizar()

        f.atualizar_projeteis(configs, tela, nave, aliens, projeteis)

        f.atualizar_aliens(configs, aliens)

        f.atualizacao_tela(configs, tela, nave, aliens, projeteis)


rodando_jogo()

''' Finalizando na 405 '''
