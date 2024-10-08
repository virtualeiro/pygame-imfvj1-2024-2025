#Seção para importar bibliotecas
import pygame
import random
pygame.init()
#Seção configuração 
#opção 1 
#MAX_X=600
#MAX_Y=400
#screen = pygame.display.set_mode((MAX_X, MAX_Y))
#opção 2
DIM_SCREEN=(600,400)
screen = pygame.display.set_mode(DIM_SCREEN)

pygame.display.set_caption("Minha Janela")
running = True
while(running == True): #running tem o valor de true?
    #Gestão dos inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#Fechei ecrã
            running=False  
        elif event.type == pygame.KEYDOWN: #Carreguei em tecla
            if event.key == pygame.K_1: #A tecla era o 1
                 print("Pressionamos a tecla 1")   
    #Secção gráfica
    #COR_FUNDO=(255,255,255)
    #screen.fill(COR_FUNDO)
    screen.fill((255,255,255))
    
    RED=(255,0,0)
    #st_pos=(0,0)
    st_pos=(random.randrange(100),random.randrange(0,500)) 
    end_pos=DIM_SCREEN
    pygame.draw.line(screen, RED, st_pos, end_pos, 100)

    #actualiza o ecrã
    pygame.display.update()

pygame.quit()