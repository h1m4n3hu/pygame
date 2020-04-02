import pygame

pygame.init()

screen=pygame.display.set_mode((800,800))
title=pygame.display.set_caption("FirstGame")
clock=pygame.time.Clock()
screen.fill((0,0,255))
allsprites=pygame.sprite.Group()
xpos=200
ypos=200

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(200,200)
    def update(self):
        self.rect.x+=1
        pass
        
allsprites.add(Box())
        
pygame.draw.rect(screen,(0,255,0),[xpos,ypos,50,10])


run=True
while run:
    #code here
    xpos+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
            
    screen.fill((0,0,255))
    allsprites.update()

    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()