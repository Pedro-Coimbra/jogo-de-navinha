import pygame
import random

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Adciona Titulo e icone
pygame.display.set_caption("Jogo de Navinha")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# imagm e posicao do jogador
imgJogador = pygame.image.load("jogador.png")
jogadorX = 370
jogadorY = 480
jogadorX_change = 0

# inimigo
imgInimigo = pygame.image.load("inimigo.png")
inimigoX = random.randint(0, 800)
inimigoY = random.randint(50, 150)
inimigoX_change = 0.3
inimigoY_change = 30


def jogador(x, y):
    screen.blit(imgJogador, (x, y))


def inimigo(x, y):
    screen.blit(imgInimigo, (x, y))


# Loop do jogo
running = True
while running:
    # cor da tela
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # verifica se tecla pressionada é esquerda ou direita
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogadorX_change = -0.3
            if event.key == pygame.K_RIGHT:
                jogadorX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jogadorX_change = 0

    # Movimento do jogador
    jogadorX += jogadorX_change

    # Verifica se o jogador chegou no limite da janela
    if jogadorX <= 0:
        jogadorX = 0
    elif jogadorX >= 736:
        jogadorX = 736

    # Movimento do inimigo
    inimigoX += inimigoX_change

    if inimigoX <= 0:
        inimigoX_change = 0.3
        inimigoY += inimigoY_change
    elif inimigoX >= 736:
        inimigoX_change = -0.3
        inimigoY += inimigoY_change

    jogador(jogadorX, jogadorY)
    inimigo(inimigoX, inimigoY)
    pygame.display.update()
