# ################################
# #Boilerplate
# ################################
# import pygame
# import sys
#
#
# pygame.init()
#
# # Let's create a caption for the game wind
# pygame.display.set_caption("Hello Liam")
# screen = pygame.display.set_mode((640, 480))
#
#
# while True:
#
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         # Additional interactions with events
#
#     screen.fill(pygame.Color("Gray"))
#
#     pygame.display.update()


# ################################
# #Drawing Circle
# ################################
# API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

# ################################
# #Images
# ################################
# make and load the image
# image1 = pygame.image.load("2dogs.JPG")
#blit the image
#screen.blit(image1, (0, 0))
#            image     pos

# ################################
# #Text
# ################################
#initialize the font
# font1 = pygame.font.SysFont("comicsansms", 28)
# use the font to make the text
# caption1 = font1.render("Two Dogs", True, pygame.Color("Blue"))
# blit the render of the font to the screen
# screen.blit(caption1, ((screen.get_width()-caption1.get_width())/2,image1.get_height()-10))
#      rendered text ^         x position                                  y position


# ################################
# #Sound Effects
# ################################
#initalize the sound file to a variable, AKA: create the sound object
# sound1 = pygame.mixer.Sound("bark.wav")
# play the sound object if the mouse button has been clicked
# if event.type == pygame.MOUSEBUTTONDOWN:
#     sound1.play()

# ################################
# #Background Music
# ################################
# pygame.mixer.music.load("drums.wav")
# load the background music into the pygame ^^^^
#pygame.mixer.music.play(-1)
#pass the number of times you want to loop, -1 for infinate loop, dont pass anything to play 1 time
#pygame.mixer.music.pause() to pause the music
#pygame.mixer.music.stop() to stop the music
