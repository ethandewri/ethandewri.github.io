'''
Hello, Im Ethan Dewri and this is my snake game but with bananas.
For this program to work, you must install pygame. Heres a link:https://www.pygame.org/download.shtml
Here is refernce to where I learned this code from: https://www.youtube.com/watch?v=K5F-aGDIYaM&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq
'''

import pygame
import time
import random 

pygame.init() #initializes pygame (shows if something didn't work)

white = (255,255,255) #(red, green, blue)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
yellow = (255,223,0) #1. new background color when game ends
grey = (78,82,89) #2. new background color for in game screen
blue = (74, 239, 236) #3. snake color

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))  #tuple (800 = width, 600 = height)
pygame.display.set_caption('Slither')

icon = pygame.image.load('banana.png')
pygame.display.set_icon(icon)

img = pygame.image.load('snakeHead.png')

banana_img = pygame.image.load('banana.png')


clock = pygame.time.Clock()

AppleThickness = 30
block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("arial", 25)
medfont = pygame.font.SysFont("arial", 50)    #4. the font
largefont = pygame.font.SysFont("arial", 80)


def pause():

    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_ESCAPE:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            gameDisplay.fill(yellow)
            message_to_screen("Paused",
                                black,
                                -100,
                                size = "large")

            message_to_screen("Press ESC to continue or Q to quit.",
                              black,
                              25)
            pygame.display.update()
            clock.tick(5)
            
    

def score(score):
    text = smallfont.render("Score: "+ str(score), True, black)
    gameDisplay.blit(text, [0,0])


def randAppleGen(): #empty parameters bc AppleThickness is a constant. defined at the top. 
    randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))#/10.0)*10.0


    return randAppleX, randAppleY




def game_intro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    quit()


        
        gameDisplay.fill(yellow)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")

        message_to_screen("The Objective of the game is to eat bananas.",
                          grey,
                          -30,)
        
        message_to_screen("The more bananas you eat, the larger you get.",
                          grey,
                          10,)
        
        message_to_screen("If you run into yourself or the walls, you die!",
                          grey,
                          50,)
        
        message_to_screen("Press C to play, ESC to pause,  or Q to quit.",
                          grey,
                          180,)


        pygame.display.update()
        clock.tick(15)  #fps
                          

        
def snake(block_size,snakeList):  #block_size and snakeList are local variables. They can only be used in the loop. 

    if direction =="right":
        head = pygame.transform.rotate(img, 270)

    if direction =="left":
        head = pygame.transform.rotate(img, 90)       #These moves the snake

    if direction =="up":
        head = img
        
    if direction =="down":
         head = pygame.transform.rotate(img, 180)
        
    
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, blue, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color) 
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width /2), (display_height /2) + y_displace #y_displacement = center of text
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()
    
    while not gameExit:
        
        while gameOver == True:
            gameDisplay.fill(yellow)
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size = "large")
            message_to_screen("Press C to play again or Q to quit",
                              grey,
                              50,
                              size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size #movement in pixels
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size #movement in pixels
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size #movement in pixels
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size #movement in pixels
                    lead_x_change = 0

                elif event.key == pygame.K_ESCAPE:  #5. replaced paused key with esc. 
                    pause()
            
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
            


                  

        lead_x += lead_x_change
        lead_y += lead_y_change
        
        
        gameDisplay.fill(grey)


        
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(banana_img, (randAppleX, randAppleY)) #6. img of apple to banana


        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len (snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

    

        
        snake(block_size, snakeList)
        

        
        snake(block_size,snakeList)

        score(snakeLength-1)
        
        pygame.display.update()

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y  > randAppleY and lead_y < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

                
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            
            
            
        clock.tick(FPS) #frames per second
        

    pygame.quit()
    quit()
game_intro()
gameLoop()

