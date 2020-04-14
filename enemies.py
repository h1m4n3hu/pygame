import pygame
import random

pygame.init()

screen=pygame.display.set_mode((1200,500))
title=pygame.display.set_caption("FirstGame")
clock=pygame.time.Clock()
allsprites=pygame.sprite.Group()
enemies=pygame.sprite.Group()
vec=pygame.math.Vector2

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.pos=vec(300,375)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):        
        self.vel+=self.acc
        self.pos+=self.vel+(self.acc)/2
        self.rect.center=self.pos
box=Box()
allsprites.add(box)

class Bu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((5,5))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect()
        self.pos=vec(box.pos.x,box.pos.y)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):        
        self.vel+=self.acc
        self.pos+=self.vel+(self.acc)/2
        self.rect.center=self.pos

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((25,25))
        self.image.fill((255,100,100))
        self.rect=self.image.get_rect()
        self.pos=vec(random.randrange(100,1100),random.randrange(-100,100))
        self.vel=vec(0,random.randrange(1,4))
        self.acc=vec(0,0)
    def update(self):        
        self.vel+=self.acc
        self.pos+=self.vel+(self.acc)/2
        self.rect.center=self.pos
for i in range(0,6):
    enemy=Enemy()
    allsprites.add(enemy)
    enemies.add(enemy)

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((1200,100))
        self.image.fill((0,255,0))
        self.rect=self.image.get_rect()
        self.pos=vec(600,450)
    def update(self):        
        self.rect.center=self.pos
floor=Floor()
allsprites.add(floor)

run=True
while run:
    
    #conditional statement
    if box.pos.x<-50:
        box.pos.x=1250
    if box.pos.x>1250:
        box.pos.x=-50
    if box.pos.y>375:
        box.vel.y=0
        box.acc.y=0
    hit=pygame.sprite.spritecollide(box,enemies,False)
    if hit==True:
        print("wrectyvgu")
        
        #key_event ke liye loops
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
                    #down press pe events
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                box.vel.x=2
            if event.key==pygame.K_LEFT:
                box.vel.x=-2
            if event.key==pygame.K_SPACE:
                bu=Bu()
                allsprites.add(bu)
                bu.vel.x=2
            if box.vel.y==0:
                if event.key==pygame.K_UP:
                    box.vel.y=-3
                    box.acc.y=+0.02
                    
                    #key leave karne pe events
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                box.vel.x=0
            if event.key==pygame.K_LEFT:
                box.vel.x=0
                
    allsprites.update()
    enemies.update()
    screen.fill((0,0,255))
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()