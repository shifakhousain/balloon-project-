# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
window  = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("my awesome game")
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # fill the windows with a color to wipe away anything from last frame
    window.fill("white")
    red, green, blue=(255,0,0), (0,255,0), (0,0,255)
    pygame.draw.polygon(window,red,((491,100),(788,100),(937,357),(786,614),(491,614),(342,357)))
    pygame.draw.circle(window,green,(640,360),200)
    pygame.draw.line(window,blue,(468,392),(812,392),10)
    pygame.draw.rect(window,blue,(468,307,345,70),border_radius=5)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on window
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 30
    pygame.display.update()
