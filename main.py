import pygame
import random

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Fundo da tela
background = pygame.image.load('background.png')

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
inimigoX_change = 4
inimigoY_change = 30

# Projetil
# pronto - projetil na tela
# tiro   - projetil se movimentando
imgProjetil = pygame.image.load("laser.png")
ProjetilX = 0
projetilY = 480
projetilX_change = 0
projetilY_change = 10
projetil_estado = "pronto"

def jogador(x, y):
    screen.blit(imgJogador, (x, y))


def inimigo(x, y):
    screen.blit(imgInimigo, (x, y))

def atirar(x,y):
    global projetil_estado
    projetil_estado = "tiro"
    screen.blit(imgProjetil,(x + 31, y + 10))


# Loop do jogo
running = True
while running:
    # cor da tela
    screen.fill((0, 0, 0))
    # imagem de fundo da tela
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # verifica se tecla pressionada é esquerda ou direita
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogadorX_change = -5
            if event.key == pygame.K_RIGHT:
                jogadorX_change = 5
            if event.key == pygame.K_SPACE:
                if projetil_estado is "pronto":
                    projetilX = jogadorX
                    atirar(projetilX, projetilY)
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
        inimigoX_change = 4
        inimigoY += inimigoY_change
    elif inimigoX >= 736:
        inimigoX_change = -4
        inimigoY += inimigoY_change

    # Movinemnto da bala
    if projetilY <= 0:
        projetilY = 480
        projetil_estado = "pronto"
    if projetil_estado is "tiro":
        atirar(projetilX, projetilY)
        projetilY -= projetilY_change

    jogador(jogadorX, jogadorY)
    inimigo(inimigoX, inimigoY)
    pygame.display.update()
