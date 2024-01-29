#import
import pygame


#initialize
pygame.init()

width,height=1280,720
window =pygame.display.set_mode((width,height))
pygame.display.set_caption("my awesome game")

#initialize clock for fps
fps=30
clock = pygame.time.Clock()

#main loop
start =True
while start :
    #get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

# Display
window.fill("purple")
#set Fps
clock.tick(fps)
#window update
pygame.display.update()
pygame.display.flip()
