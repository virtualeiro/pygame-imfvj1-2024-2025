import pygame
pygame.init()

WIDTH=800
HEIGHT=600
dimensoes=(WIDTH,HEIGHT)
screen = pygame.display.set_mode(dimensoes) 
#screen = pygame.display.set_mode((800,600)) 

def camada_fundo(val):
   cor=(200,150,125)
   rect1=(val, 200, 1760, 560) 
   pygame.draw.ellipse(screen,cor, rect1)
   rect2=(val-1500, 200, 1760, 560)    
   pygame.draw.ellipse(screen,cor, rect2)   

def arvore(x,y,r):
   pygame.draw.rect(screen,(255,255,0), (x-r/4,y+r/2, r/2, r*2))
   pygame.draw.circle(screen,(0,255,0), (x,y),r)

def camada_arvores(val):
     arvore(val,400,40)
     arvore(val+50,400,30)
     arvore(val+100,425,20)
     arvore(val-200,425,20)
     arvore(val-550,425,10)
     arvore(val-1550,425,10)

def camada_estatica():
   pygame.draw.rect(screen,(255,125,0), (0, 0, 100, HEIGHT))
   pygame.draw.rect(screen,(255,125,0), (WIDTH-100, 0, 100, HEIGHT))
   pygame.draw.rect(screen,(255,125,0), (0, 0, WIDTH, 100))
   pygame.draw.rect(screen,(255,125,0), (0, HEIGHT-100, WIDTH, 100))
   

desistir=False
x_arvores=0
x_fundo=-200
while(desistir==False):
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
          desistir=True
   screen.fill((100,100,250))
   
   x_fundo=x_fundo+0.1
   camada_fundo(x_fundo)
   x_arvores=x_arvores+0.5
   camada_arvores(x_arvores)
   camada_estatica()
   pygame.display.update() 
pygame.quit()