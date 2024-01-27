import pygame
import os
import random

TELA_LARGURA = 500
TELA_ALTURA = 800

# Importação das imagens
IMAGEM_CANO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_FUNDO = pygame.transform.scale2x(
    pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGENS_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(
        os.path.join('imgs', 'bird3.png')))
]

# Definindo a fonte das letras
pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)


# CRIANDO AS CLASSES PARA CADA UM DOS OBJETOS (Depois eu faço modularização nessas classes)

class Passaro:
    IMGS = IMAGENS_PASSARO

    # Animações de rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y

        # Parametros auxiliares
        self.tempo = 0
        self.contagem_imagem = 0

        # Imagem do passaro
        self.imagem = IMGS[0]

    # Criando a função para fazer o passáro pular
    def pular(self):
        self.velocidade = 10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):  # Rever aula 04 para entender melhor essa parte do códgido    
        # Calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo * 2) + self.velocidade * self.tempo

        # Restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2

        self.y += deslocamento

        # Ângulo do passáro
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA

        else:
            if self.angulo > - 90:
                self.angulo -= self.VELOCIDADE_ROTACAO


class Chao:
    pass


class Cano:
    pass
