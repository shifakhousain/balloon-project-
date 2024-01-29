import pygame

# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("my awesome game")
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
    font = pygame.font.Font('../Resources/yasbanu.ttf',100)
    text = font.render("My Awesome Game",True,(50,50,50))
    window.blit(text,(350,300))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on window
    pygame.display.flip()
    pygame.display.update()

    clock.tick(30)