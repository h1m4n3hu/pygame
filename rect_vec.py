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
        self.vel+=self.acc    #v=v+at === v+=a
        self.pos+=self.vel+(self.acc)/2   #s+=u+1/2a
        self.rect.center=self.pos
        
allsprites.add(Box())

run=True
while run:
    #code here
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
            
    allsprites.update()
    screen.fill((0,0,255))
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()