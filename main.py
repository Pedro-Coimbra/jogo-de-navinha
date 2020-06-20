import pygame
import random
import math
from pygame import mixer

# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

#Som de fundo
mixer.music.load('background.wav')
mixer.music.play(-1)

# Fundo da tela
background = pygame.image.load('background.png')

# Adciona Titulo e icone
pygame.display.set_caption("Jogo de Navinha")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Imagm e posicao do jogador
imgJogador = pygame.image.load("jogador.png")
jogadorX = 370
jogadorY = 480
jogadorX_change = 0

# Inimigo
imgInimigo = []
inimigoX = []
inimigoY = []
inimigoX_change = [] 
inimigoY_change = []
numero_de_inimigos = 5
for x in range(numero_de_inimigos):
    imgInimigo.append(pygame.image.load("inimigo.png"))
    inimigoX.append(random.randint(0, 735))
    inimigoY.append(random.randint(50, 150))
    inimigoX_change.append(4)
    inimigoY_change.append(30)

# Projetil
# pronto - projetil na tela
# tiro   - projetil se movimentando
imgProjetil = pygame.image.load("laser.png")
projetilX = 0
projetilY = 480
projetilX_change = 0
projetilY_change = 10
projetil_estado = "pronto"
 
# Pontuação
pontuacao = 0
font_pontuacao = pygame.font.Font('freesansbold.ttf', 22)
pontuacaoX = 10
pontuacaoY = 10

# Texto Fim de Jogo
font_fim_jogo = pygame.font.Font('freesansbold.ttf', 50)

def mostrar_pontuacao(x, y):
    pontos = font_pontuacao.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    screen.blit(pontos, (x, y))

def jogador(x, y):
    screen.blit(imgJogador, (x, y))

def inimigo(x, y, i):
    screen.blit(imgInimigo[i], (x, y))

def atirar(x,y):
    global projetil_estado
    projetil_estado = "tiro"
    screen.blit(imgProjetil,(x + 31, y + 10))

def isColisao(inimigoX, inimigoY, projetilX, projetilY):
    distancia = math.sqrt((math.pow(inimigoX-projetilX, 2)) + (math.pow(inimigoY-projetilY, 2)))
    if distancia < 27:
        return True
    else:
        return False

def fim_de_jogo_texto():
    fim_jogo_texto = font_fim_jogo.render("Fim de Jogo", True, (255, 255, 255))
    screen.blit(fim_jogo_texto, (250, 250))

def produzir_som_efeito(arquivo_som):
    som = mixer.Sound(arquivo_som)
    som.play()

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
                    produzir_som_efeito('laser.wav')
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
    for i in range(numero_de_inimigos):
        # Fim do Jogo
        if inimigoY[i] > 440:
            for x in range(numero_de_inimigos):
                inimigoY[x] = 2000
            
            fim_de_jogo_texto()
            break

        inimigoX[i] += inimigoX_change[i]
        if inimigoX[i] <= 0:
            inimigoX_change[i] = 2
            inimigoY[i] += inimigoY_change[i]
        elif inimigoX[i] >= 736:
            inimigoX_change[i] = -2
            inimigoY[i] += inimigoY_change[i]
        
        # Colisão
        colisao = isColisao(inimigoX[i], inimigoY[i], projetilX, projetilY)
        if colisao:
            produzir_som_efeito('explosion.wav')
            projetilY = 480
            projetil_estado = "pronto"
            pontuacao += 1
            inimigoX[i] = random.randint(0, 735)
            inimigoY[i] = random.randint(50, 150)
        
        inimigo(inimigoX[i], inimigoY[i], i)

    # Movimento da bala
    if projetilY <= 0:
        projetilY = 480
        projetil_estado = "pronto"
    if projetil_estado is "tiro":
        atirar(projetilX, projetilY)
        projetilY -= projetilY_change

    jogador(jogadorX, jogadorY)
    mostrar_pontuacao(pontuacaoX, pontuacaoY)
    pygame.display.update()