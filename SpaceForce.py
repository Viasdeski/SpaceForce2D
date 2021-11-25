import pygame
import time
import random

from pygame.display import Info

from funcoes import limparTela,criaBanco, leBanco,escreveBanco,insereDados, verificaEmail 


pygame.init()

inicio = True

Info = '----- Players -----'

criaBanco()
leBanco()

nomePlayer = input("Digite o seu nome: ").upper()
emailPlayer = input("Agora digite seu e-mail: ").lower()

dados = insereDados(leBanco(),nomePlayer,emailPlayer)

escreveBanco(dados)

limparTela()



while inicio:
    pygame.display.set_caption("Space Force")
    icon = pygame.image.load("assets/icone.png")
    pygame.display.set_icon(icon)

    largura = 640 
    altura = 480

    configTela = (largura,altura)
    gameDisplay = pygame.display.set_mode(configTela)

    relogio = pygame.time.Clock()

    colorBase = (255, 255, 255)
    colorFont = (255,255,255)


    player = pygame.image.load('assets/nave.png')
    pygame.transform.scale(player,[70,70])


    asteroide = pygame.image.load('assets/asteroide.png')

    fundo = pygame.image.load("assets/back.jpg")
    over = pygame.image.load("assets/morreu.png")
    lua = pygame.image.load("assets/lua.png")

    explosaoSound = pygame.mixer.Sound("assets/explosao.wav")


    def desenhaTela(pontos):
        pygame.Rect(100,100,100,100)
        gameDisplay.fill((0,0,0))
        gameDisplay.blit(fundo,(0,0))
        placar(pontos)

    def posicaoPlayer(x,y,altura,largura):
        recPlayer = gameDisplay.blit(player, (x,y,altura,largura))
        return recPlayer

    def posicaoAsteroide(x,y,altura,largura):
        recAsteroide = gameDisplay.blit(asteroide,(x,y,altura,largura))
        return recAsteroide

    def posicaoLua(x,y,altura,largura):
        recArma = gameDisplay.blit(lua,(x,y,altura,largura))
        return recArma


    def text_objects(text, font):
        textSurface = font.render(text, True, colorFont )

        return textSurface, textSurface.get_rect()

    def escreverTela(text):
        fonte = pygame.font.Font("freesansbold.ttf", 70)
        TextSurf, TextRect = text_objects(text, fonte)
        TextRect.center = ((largura/2, altura/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(5)
        game()

    def placar(contador):
        fonte = pygame.font.SysFont(None, 30)
        texto = fonte.render("Pontuação:"+str(contador), True, colorFont)
        gameDisplay.blit(texto, (10, 10))

    def dead(inicio):
        pygame.mixer.Sound.play(explosaoSound)
        pygame.mixer.music.stop()
        gameDisplay.blit(over,(-500, -150))
        escreverTela("Você falhou!")

        return inicio


    def apaga():
        player.set_alpha(0)
        asteroide.set_alpha(0)
    
    

    while True:
        def game():
            pygame.mixer.music.load("assets/loop.mp3")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)

            movimentoX = 0
            movimentoY = 0
            velocidade = 10

            asteroideX = random.randrange(0, largura)
            asteroideY = -50

            alturaPlayer = 100
            larguraPlayer = 100

            alturaAsteroide = 60
            larguraAsteroide = 60
            velocidadeAsteroide = 3

            alturaLua = 30
            larguraLua = 40

            posicaoPlayerX = largura/2
            posicaoPlayerY = altura/2


            pontos = 0

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            movimentoY = velocidade *-1 

                        elif event.key == pygame.K_DOWN:
                            movimentoY =  velocidade

                        if event.key == pygame.K_LEFT:
                            movimentoX = velocidade *-1

                        elif event.key == pygame.K_RIGHT:
                            movimentoX = velocidade

                            
                    if event.type == pygame.KEYUP:
                        movimentoX = 0
                        movimentoY = 0
                        

                posicaoPlayerY += movimentoY
                posicaoPlayerX += movimentoX



                if posicaoPlayerY < 0:
                    posicaoPlayerY = 0

                elif posicaoPlayerY > altura - alturaPlayer:
                    posicaoPlayerY = altura - alturaPlayer

                if posicaoPlayerX < 0:
                    posicaoPlayerX = 0

                elif posicaoPlayerX > largura - larguraPlayer:
                    posicaoPlayerX = largura - larguraPlayer
                        
                        
                pygame.display.update()  
                desenhaTela(pontos)
                recPlayer = posicaoPlayer(posicaoPlayerX,posicaoPlayerY, alturaPlayer,larguraPlayer)

                asteroideY = asteroideY + velocidadeAsteroide
                recAsteroide = posicaoAsteroide(asteroideX, asteroideY,alturaAsteroide,larguraAsteroide)

                recLua = posicaoLua((posicaoPlayerX + 31),(posicaoPlayerY - 20),alturaLua,larguraLua)

                if asteroideY > altura:
                    asteroideY = -50
                    asteroideX = random.randrange(0, largura)
                    pontos += 1
                    velocidadeAsteroide += 1.25

                elif asteroideX > largura - larguraAsteroide:
                    asteroideX = largura - larguraAsteroide

                if (pygame.Rect.colliderect(recPlayer, recAsteroide) == 1 or (pygame.Rect.colliderect(recLua, recAsteroide) == 1)):
                    dead(inicio)
                    apaga()
                    break

                posicaoPlayer(posicaoPlayerX, posicaoPlayerY,alturaPlayer,larguraPlayer)
                posicaoAsteroide(asteroideX, asteroideY,alturaAsteroide,larguraAsteroide)
                pygame.display.update()
                relogio.tick(60)

                

         

        game()

       


