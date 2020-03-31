import pygame

pygame.init()

screen=pygame.display.set_mode((400,400))
title=pygame.display.set_caption("FirstGame")
clock=pygame.time.Clock()

run=True
while run:
    print("Hello World!")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
            
    screen.fill((0,0,255)) #r,g,b
    pygame.display.flip()
pygame.quit()