
# import sys
import pygame
from configs import Configuracoes
from nave import Nave
import game_funcoes as gf  # gf vai ganhar as propriedades de game_funcoes

''' O módulo pygame contém as funcionalidades necessárias para criar um jogo. 
Usaremos o módulo sys para sair do jogo quando o usuário desistir. '''


def iniciar_jogo():
    # Função para dar inicialização no jogo
    pygame.init()
    config = Configuracoes()

    tela = pygame.display.set_mode(
        (config.tela_largura, config.tela_altura))

    pygame.display.set_caption('ALIEN INVADER!!')

    # Criando uma espaçonave na tela
    nave = Nave(tela)

    # Iniciando o laço principal do jogo
    while True:
        # Observa eventos de teclado e mouse
        gf.adm_events(nave)
        nave.atualizar()
        gf.att_tela(config, tela, nave)


iniciar_jogo()
