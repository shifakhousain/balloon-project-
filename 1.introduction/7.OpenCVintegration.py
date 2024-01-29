import pygame
import cv2
import numpy as np

# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("my awesome game")


running = True
#webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # fill the window with a color to wipe away anything from last frame
    #window.fill("white")
    #open camera (cv)
    success,img = cap.read()


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on window
    #pygame.display.flip()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    frame =pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))

    clock.tick(30)

    pygame.display.update()# limits FPS to 60

