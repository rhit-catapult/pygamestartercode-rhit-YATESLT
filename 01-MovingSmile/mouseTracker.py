import pygame
import sys
import math


def main():
    pygame.init()
    pygame.display.set_caption("Moving mouse tracker")
    screen = pygame.display.set_mode((640, 480))

    eye_delta_x = 0
    eye_delta_y = 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        # TODO 4: Set the clock speed to 60 fps
        for event in pygame.event.get():
           # print(event)
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys
            if event.type == pygame.KEYDOWN:

                pressed_keys = pygame.key.get_pressed()
                #print(pressed_keys)


                if pressed_keys[pygame.K_UP]:
                    eye_delta_y -= 5

                if pressed_keys[pygame.K_DOWN]:
                    eye_delta_y += 5

        screen.fill((255, 255, 255))  # white

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            eye_delta_x -= 5

        if pressed_keys[pygame.K_RIGHT]:
            eye_delta_x += 5

    # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)



        pygame.draw.circle(screen, (255, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 225, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), return_pupil_pos(240,160, 7, pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],25), 7)  # black pupil

        pygame.draw.circle(screen, (225, 225, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398+eye_delta_x,162+eye_delta_y), 7)  # black pupil

        # TODO 1: Draw a nose
        # Suggestion: color (80,0,0) location (320,245), radius 10
        pygame.draw.circle(screen, (80,0,0), (320, 245), 20)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        pygame.draw.rect(screen, (0,0,0), (230, 320, 180, 30))

        pygame.display.update()


def return_pupil_pos(xEye, yEye, rPup, xMouse, yMouse, rEye):
    radius = rEye - rPup

    xPup = xEye + (radius((xMouse-xEye)/math.sqrt((xMouse-xEye)**2+(yMouse-yEye)**2)))
    yPup = yEye + (radius((yMouse-yEye)/math.sqrt((xMouse-xEye)**2+(yMouse-yEye)**2)))
    giveBack = (xPup, yPup)
    print(giveBack)
    return giveBack


main()
