import pygame

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800,600))

# Adciona Titulo e icone
pygame.display.set_caption("Jogo de Navinha")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# imagm e posicao do jogador
imgJogador = pygame.image.load("jogador.png")
jogadorX   = 370
jogadorY   = 480

def jogador():
    screen.blit(imgJogador, (jogadorX, jogadorY))

# Loop do jogo
running = True
while running:
    # cor da tela
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jogador()
    pygame.display.update()