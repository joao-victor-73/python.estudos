import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

# Importação das imagens
IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_FUNDO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png')))
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

# Definindo a fonte das letras
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


# CRIANDO AS CLASSES PARA CADA UM DOS OBJETOS (Depois eu faço modularização nessas classes)

class Passaro:
    pass

class Chao:
    pass

class Cano:
    pass