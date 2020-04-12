import pygame
import os

pygame.init()

screen=pygame.display.set_mode((1200,500))
title=pygame.display.set_caption("FirstGame")
clock=pygame.time.Clock()
allsprites=pygame.sprite.Group()
vec=pygame.math.Vector2
picfolder=os.path.dirname(__file__)
imgfolder=os.path.join(picfolder,"imgs")
BLACK=(0,0,0)

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.walk=False
        self.curframe=0
        self.lastupdate=0
        self.loadimage()
        self.rect=self.image.get_rect()
        self.image.set_colorkey((0,0,0))
        self.pos=vec(150,300)
        self.vel=vec(2,0)
        self.acc=vec(0,0)
    def loadimage(self):
        self.runimg=[(pygame.image.load(os.path.join(imgfolder,"run_1.png"))),
                     (pygame.image.load(os.path.join(imgfolder,"run_2.png"))),
                     (pygame.image.load(os.path.join(imgfolder,"run_3.png"))),
                     (pygame.image.load(os.path.join(imgfolder,"run_4.png")))]
        self.walkframe=[]
        for frame in self.runimg:
            self.walkframe.append(pygame.transform.flip(frame,True,False))
        self.image=self.runimg[0]
    def update(self):
        self.vel.x+=self.acc.x
        self.pos.y+=self.vel.y+0.5*self.acc.y
        self.rect.center=self.pos
        self.animate()
    def jump(self):
        box.image=pygame.image.load(os.path.join(imgfolder,"jump_0.png"))
    def animate(self):
        now=pygame.time.get_ticks()
        if not self.walk:
            if now-self.lastupdate>70:
                self.lastupdate=now
                self.curframe=(self.curframe+1)%len(self.runimg)
                self.image=self.runimg[self.curframe]
            if box.vel.x==0:
                box.image=pygame.image.load(os.path.join(imgfolder,"idle_0.png"))       
            
box=Box()
allsprites.add(box)

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




class Plank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((300,40))
        self.image.fill((0,255,255))
        self.rect=self.image.get_rect()
        self.pos=vec(800,250)
    def update(self):        
        self.rect.center=self.pos
plank=Plank()
allsprites.add(plank)




run=True
while run:
    
    walkcount=0
    
    
    
    
    
    if box.pos.x<-50:
        box.pos.x=1250
    if box.pos.x>1250:
        box.pos.x=-50
    if box.pos.y>375:
        box.vel.y=0
        box.acc.y=0
        
    if box.vel.y>0:
        if box.pos.x<950 and box.pos.x>650:
            if box.pos.y<225 and box.pos.y>205:
                box.vel.y=0
                box.acc.y=0
    if box.pos.x>950 or box.pos.x<650:
        if box.pos.y<225 and box.pos.y>205:
            #box.vel.y=0
            box.acc.y=0.02


    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                box.vel.x=2
            if event.key==pygame.K_LEFT:
                box.vel.x=-2
                
            if box.vel.y==0:
                if event.key==pygame.K_UP:
                    box.vel.y=-3
                    box.acc.y=+0.02
                    
                    
                    
                    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                box.vel.x=0
            if event.key==pygame.K_LEFT:
                box.vel.x=-0
                
    allsprites.update()
    screen.fill((0,0,255))
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()