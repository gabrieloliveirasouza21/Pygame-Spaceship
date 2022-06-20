import pygame
import os

#criando a interface do jogo
LARGURA, ALTURA = 900, 500 # 2) definindo a altura e largura
JANELA = pygame.display.set_mode((LARGURA,ALTURA))#1) dentro dos parenteses é onde coloca o tamanho da janela
pygame.display.set_caption("Joguinho com PyGame")
FPS = 60 # 8) definindo a quantidade de fps do jogo
NAVE_AMARELA = pygame.image.load(os.path.join('assets','spaceship_yellow.png'))
NAVE_VERMELHA = pygame.image.load(os.path.join('assets','spaceship_red.png'))
NAVE_AMARELA_TAMANHO = pygame.transform.rotate(pygame.transform.scale(NAVE_AMARELA, (55,40)),90) # 10) definindo o tamanho 
NAVE_VERMELHA_TAMANHO = pygame.transform.rotate(pygame.transform.scale(NAVE_VERMELHA, (55,40)), 270) # 10) definindo o tamanho 


def design_da_janela(vermelha, amarela): 
    JANELA.fill((255,255,255)) # 5) colorindo a tela (dentro da main primeiro)
    JANELA.blit(NAVE_AMARELA_TAMANHO, (amarela.x, amarela.y)) # 9) permite que a gente coloque alumas coisas na superfície do jogo // antes : (NAVE_AMARELA_TAMANHO, (300,100))
    JANELA.blit(NAVE_VERMELHA_TAMANHO,(vermelha.x, vermelha.y)) # antes : (NAVE_VERMELHA_TAMANHO,(700, 100))
    pygame.display.update()# 6) atualizando a janela (dentro da main primeiro)


def main (): # 3) aqui nessa função onde vai ser o event loop, verificando colisões, atualizar a pontuação, ficar atualizando o jogo.
    vermelha = pygame.Rect(700,300,55,40) # para fazer a movimentação
    amarela = pygame.Rect(100,300,55,40)
 

    frames = pygame.time.Clock() # definindo quantas atualizações por segundo
    rodando = True
    while rodando :
        frames.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False 
        # 7) criar uma função para apenas a parte do design
        vermelha.x += 1 
        design_da_janela(vermelha,amarela)
              
    pygame.quit()

if __name__ == "__main__" : # 4)só vai rodar o jogo se rodar o arquivo diretamente
    main()
