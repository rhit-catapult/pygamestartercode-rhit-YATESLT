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

# ################################
# #Mouse movement (Getting mouse position)
# ################################
# pygame.mouse.get_pos()
# or
# pygame.event.event_pos()   ??? <--- not sure if this works

# ################################
# #Object Oriented Programming
# ################################
# Objects know stuff (instance variables)
# Objects can do stuff (methods
# EXAMPLE:
# class Hero:
#     def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
#         """ Creates a Hero sprite (Mike) that does not move. If hit by rain he'll put up his umbrella. """
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.image_umbrella = pygame.image.load(with_umbrella_filename)
#         self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
#         self.last_hit_time = 0
# This is a class, with a constructor (__init__)
# self represents local variables that are inside the "factory"
# Method example:
# def hit_by(self, raindrop)
#     """ Returns true if the given raindrop is hitting this Hero, otherwise false. """
#     hero_hit_box = pygame.Rect(self.x, self.y, self.image_no_umbrella.get_width(),self.image_no_umbrella.get_height())
#
#     return hero_hit_box.collidepoint(raindrop.x, raindrop.y)



