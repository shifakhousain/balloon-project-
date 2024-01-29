import pygame

# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("my awesome game")

#load Images
imgBackground = pygame.image.load("../Resources/backgroundblue.jpg").convert()
imgBalloonRed = pygame.image.load("../Resources/balloonimg.png").convert_alpha()
rectballon=imgBalloonRed.get_rect()

rectNew =pygame.Rect(500,0,200,200)

running = True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # fill the window with a color to wipe away anything from last frame
    window.fill("white")
    print(rectballon.colliderect(rectNew))
    rectballon.x += 5


    window.blit(imgBackground,(0,0))
    #pygame.draw.rect(window, (0, 255, 0), rectballon)
    pygame.draw.rect(window, (0, 255, 0), rectNew)
    window.blit(imgBalloonRed, rectballon)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on window
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

