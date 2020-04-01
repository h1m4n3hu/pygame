import pygame

pygame.init()

screen=pygame.display.set_mode((400,400))
title=pygame.display.set_caption("FirstGame")
clock=pygame.time.Clock()
screen.fill((0,0,255))
allsprites=pygame.sprite.Group()


class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.center=(200,200)
allsprites.add(Box())
        
pygame.draw.rect(screen,(0,255,0),[200,200,50,10])

run=True
while run:
    #code here
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
            
    allsprites.update()
    allsprites.draw(screen)
    pygame.display.flip()
pygame.quit()