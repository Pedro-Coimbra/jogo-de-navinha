import pygame

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


def jogador(x, y):
    screen.blit(imgJogador, (x, y))


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

    if jogadorX <= 0:
        jogadorX = 0
    elif jogadorX >= 736:
        jogadorX = 736

    jogadorX += jogadorX_change
    jogador(jogadorX, jogadorY)
    pygame.display.update()
