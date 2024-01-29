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

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on window
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

