import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Window")
clock = pygame.time.Clock()

x=0
y=0
ang=0
horizon=300
FPS=12
a=1
y=horizon
dias_semana=["Segunda","Terça","Quarta","Quinta","Sexta","Sabado","Domingo"]

def grafico_pergunta_1():
  global x,y,ang,a
  ang=ang+math.pi/100  
  y =  10*math.sin(ang)
  pygame.draw.circle(screen, (255,0,0), (x,y+100),1)
  x=x+0.5

def grafico_pergunta_2():
  color=(random.randrange(0,256), random.randrange(0,256),random.randrange(0,256))
  position=(random.randrange(200,600),random.randrange(200,400) )
  pygame.draw.circle(screen, color, position,10, 4)

def grafico_pergunta_3():
  print(dias_semana[random.randrange(0,7)])
  print(dias_semana[random.randrange(7)])
  print(dias_semana[random.randrange(len(dias_semana))])
  print(random.choice(dias_semana))

position = pygame.Vector2(100,240)
velocity = pygame.Vector2(0,-1)
speed=2

def grafico_pergunta_4():
  global position, velocity
  screen.fill((0,0,0))
  position=position+velocity*speed
  pygame.draw.circle(screen, (255,0,0), position, 10, 12)  
  pygame.draw.line(screen, (255,0,0), position, (position.x, position.y+30), 1)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    grafico_pergunta_1()
    #grafico_pergunta_2()
    #grafico_pergunta_3()
    #grafico_pergunta_4()
    #print("Para aumentar a velocidade do balão duplicava o valor de speed.")
    #print("Deltatime é o tempo que passa entre duas frames, entre dois updates.")
    #print("Podemos tentar controlar com clock.tick()")
    clock.tick(FPS)
    pygame.display.flip()
 
pygame.quit()