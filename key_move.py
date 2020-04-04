import pygame

pygame.init()

screen=pygame.display.set_mode((800,800))
title=pygame.display.set_caption("FirstGame")
clock=pygame.time.Clock()
allsprites=pygame.sprite.Group()
vec=pygame.math.Vector2

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.pos=vec(200,20)
        self.vel=vec(0,0)
        self.acc=vec(0,0)
    def update(self):
        #self.acc.y=0.05
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.vel.x=1
        if keys[pygame.K_LEFT]:
            self.vel.x=-1
        if keys[pygame.K_UP]:
            self.vel.y=-1
        
        self.vel+=self.acc    #v=v+at === v+=a
        self.pos+=self.vel+(self.acc)/2   #s+=u+1/2a
        self.rect.center=self.pos

box=Box()
allsprites.add(box)

run=True
while run:
    #code here
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                box.acc.x=0.01
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                box.acc.x=0
                box.vel.x=0   
        
    allsprites.update()
    screen.fill((0,0,255))
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()