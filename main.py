import pygame
import random
import math
from pygame import mixer


# Botão
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


# Inicializa o pygame
pygame.init()

# Cria a tela
screen = pygame.display.set_mode((800, 600))

# Caixa de texto
base_font = pygame.font.Font(None, 32)
texto = ''

text_input = pygame.Rect(255, 200, 140, 32)
cor_ativa = pygame.Color('white')
cor_passiva = pygame.Color('gray15')
cor = cor_passiva
ativa = False

# Jogar novamente
reiniciar = False

# Som de fundo
mixer.music.load('background.wav')
mixer.music.play(-1)

# Fundo da tela
background = pygame.image.load('background.png')

# Adciona Titulo e icone
pygame.display.set_caption("Space Survival")
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
mais_movimento = 2

for x in range(numero_de_inimigos):
    imgInimigo.append(pygame.image.load("inimigo.png"))
    imgInimigo.append(pygame.image.load("inimigo2.png"))
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

font = pygame.font.Font('freesansbold.ttf', 22)
# Pontuação
pontuacao = 0
pontuacaoX = 10
pontuacaoY = 10
# Dificuldade
dificuldade = "muito fácil"
dificuldadeX = 520
dificuldadeY = 10
# Nickname
nickname = ''
nicknameX = 10
nicknameY = 570

# Texto Fim de Jogo
font_fim_jogo = pygame.font.Font('freesansbold.ttf', 50)


def mostrar_pontuacao(x, y):
    pontos = font.render("Pontuação: " + str(pontuacao), True, (255, 255, 255))
    screen.blit(pontos, (x, y))


def mostrar_dificuldade(x, y):
    dif = font.render("Dificuldade: " + str(dificuldade), True, (255, 255, 255))
    screen.blit(dif, (x, y))


def mostrar_nickname(x, y):
    nome = font.render("Nome: " + str(nickname), True, (255, 255, 255))
    screen.blit(nome, (x, y))


def jogador(x, y):
    screen.blit(imgJogador, (x, y))


def inimigo(x, y, i):
    screen.blit(imgInimigo[i], (x, y))


def atirar(x, y):
    global projetil_estado
    projetil_estado = "tiro"
    screen.blit(imgProjetil, (x + 31, y + 10))


def isColisao(inimigoX, inimigoY, projetilX, projetilY):
    distancia = math.sqrt((math.pow(inimigoX - projetilX, 2)) + (math.pow(inimigoY - projetilY, 2)))
    if distancia < 27:
        return True
    else:
        return False


def fim_de_jogo_texto():
    fim_jogo_texto = font_fim_jogo.render("Fim de Jogo", True, (255, 255, 255))
    screen.blit(fim_jogo_texto, (250, 250))
    botaoJogarNovamente = button((0, 255, 0), 205, 320, 380, 80, 'Jogar novamente')
    botaoJogarNovamente.draw(screen, (0, 0, 0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoJogarNovamente.isOver(pos):
                print("deu bom")
            else:
                return False


def produzir_som_efeito(arquivo_som):
    som = mixer.Sound(arquivo_som)
    som.play()


before_running = True
while before_running:
    # cor da tela
    screen.fill((0, 0, 0))
    # imagem de fundo da tela
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, cor, text_input, 2)

    text_surface = base_font.render(texto, True, (255, 255, 255))
    screen.blit(text_surface, (text_input.x + 5, text_input.y + 5))

    text_input.w = max(300, text_surface.get_width() + 10)

    botaoJogarNovamente = button((0, 255, 0), 205, 320, 380, 80, 'Jogar')
    botaoJogarNovamente.draw(screen, (0, 0, 0))

    botaoJogar = button((0,255,0), 205,320,380,80,'Jogar')
    botaoJogar.draw(screen,(0,0,0))
    
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if botaoJogar.isOver(pos):
                print("O Nome está vazio")
                if texto:
                    print("Nome: ", texto)
                    with open('ranking.txt','w') as arquivo:
                        arquivo.write(str(texto))
                    nickname = texto
                    before_running = False
                    # Loop do jogo
                    running = True

        if event.type == pygame.QUIT:
            running = False
            before_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_input.collidepoint(event.pos):
                ativa = True

        if event.type == pygame.KEYDOWN:
            if ativa == True:
                if event.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]
                else:
                    texto += event.unicode

    if ativa:
        cor = cor_ativa
    else:
        cor = cor_passiva
    pygame.display.update()

while running:
    # cor da tela
    screen.fill((0, 0, 0))
    # imagem de fundo da tela
    screen.blit(background, (0, 0))
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
                if projetil_estado == "pronto":
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

            if fim_de_jogo_texto():
                print("teste")

        inimigoX[i] += inimigoX_change[i]

        if inimigoX[i] <= 0:
            inimigoX_change[i] = mais_movimento
            inimigoY[i] += inimigoY_change[i]
        elif inimigoX[i] >= 736:
            inimigoX_change[i] = -mais_movimento
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
            if pontuacao >= 60:
                dificuldade = "cabuloso"
                mais_movimento += 1
            elif pontuacao == 50:
                dificuldade = "extremo"
                mais_movimento += 1
            elif pontuacao == 40:
                dificuldade = "muito dificil"
                mais_movimento += 1
            elif pontuacao == 30:
                dificuldade = "dificil"
                mais_movimento += 1
            elif pontuacao == 20:
                dificuldade = "médio"
                mais_movimento += 1
            elif pontuacao == 10:
                dificuldade = "fácil"
                mais_movimento += 1
        inimigo(inimigoX[i], inimigoY[i], i)

    # Movimento da bala
    if projetilY <= 0:
        projetilY = 480
        projetil_estado = "pronto"
    if projetil_estado == "tiro":
        atirar(projetilX, projetilY)
        projetilY -= projetilY_change

    jogador(jogadorX, jogadorY)
    mostrar_pontuacao(pontuacaoX, pontuacaoY)
    mostrar_dificuldade(dificuldadeX, dificuldadeY)
    mostrar_nickname(nicknameX, nicknameY)
    pygame.display.update()
