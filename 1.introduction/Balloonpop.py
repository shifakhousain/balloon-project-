import random

import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("balloon pop")



#webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#images
imgBalloon = pygame.image.load("../Resources/balloonimg.png").convert_alpha()
rectBalloon = imgBalloon.get_rect()
rectBalloon.x,rectBalloon.y= 500,500
speed = 5

#hand Detection
detector =HandDetector(detectionCon=0.8, maxHands=2)
def resetBalloon():
    rectBalloon.x= random.randint(100,img.shape[1]-100)
    rectBalloon.y=img.shape[0]+50

running = True
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
    img =cv2.flip(img,1)
    #find Hands programs
    hands,img =detector.findHands(img,flipType=False)


    # RENDER YOUR GAME HERE
    #logic here

    # flip() the display to put your work on window
    #pygame.display.flip()
    rectBalloon.y -= speed

    if rectBalloon.y < 0:
        resetBalloon()
        speed+=1

    if hands:
        hand = hands[0]
        x, y = hand["lmList"][8]
        if rectBalloon.collidepoint(x, y):
            resetBalloon()




    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    frame = pygame.surfarray.make_surface(imgRGB).convert()
    #frame =pygame.transform.flip(frame,True,False)
    window.blit(frame,(0,0))

    window.blit(imgBalloon,rectBalloon)
    pygame.display.update()



    clock.tick(30)  # limits FPS to 60