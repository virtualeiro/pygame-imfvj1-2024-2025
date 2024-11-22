import pygame
import random
from pygame.math import Vector2
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Window")
clock = pygame.time.Clock()

posRed=(320,240)
posBlue=Vector2(320,240)
velRed =Vector2(1,0)
velBlue=Vector2(-1,0)
RED,BLUE=(255,0,0),(0,0,255)
speedRed, speedBlue = 2, 0.1 
def graficos():
    global posRed, posBlue, velRed, velBlue
    screen.fill((0,0,0))
    #movimento
    pygame.draw.circle(screen, RED, posRed, 30)
    pygame.draw.circle(screen, BLUE, posBlue, 30)
    posRed = posRed + velRed*speedRed
    posBlue = posBlue + velBlue*speedBlue
    #determinação da direção 
    a=Vector2.normalize(velRed)
    b=Vector2.normalize(velBlue)

#Atencao fazer operacao com vetores normalizados
#Se o dot product (produto interno) for igual a 1, 
#Significa que ambos têm a mesma direção. 
    if(Vector2.dot(a, b)==1):
           print("Mesma direção")
#Se o dot product for 0, 
#significa que são perpendiculares um ao outro
    elif(Vector2.dot(a, b)==0): 
           print("Perpendicular")
#Finalmente se o dot.product for -1, 
#significa que ambos os vetores estão a movimentar-se em direções opostas
    elif(Vector2.dot(a, b)==-1): 
           print("Direções opostas") 
    else :print("Não ortogonal nem paralela")
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    graficos()

    pygame.display.flip()
    clock.tick(30)
pygame.quit()