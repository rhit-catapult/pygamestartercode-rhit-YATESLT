import pygame
import sys
import random
import math


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
    def move(self, ballList):

        self.x  += self.speed_x
        self.y += self.speed_y

        #CHECK TO SEE IF THE BALL IS TOUCHING THE SIDE
        if self.x -self.radius < 0 or self.x + self.radius > self.screen.get_width():
            self.speed_x *= -1
        if self.y - self.radius < 0 or self.y + self.radius > self.screen.get_height():
            self.speed_y *= -1


        #CHECK TO SEE IF YOUR TOUCHING ANOTHER BALL
        for ball in ballList:
            if self.x == ball.x and self.y == ball.y:
                continue
            #Look at distnace between centers of balls, look to see if the distances is less than 1 of the 2 radiuses.
            distance = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
            # print(distance)
            if distance < (self.radius*2)+5: #change the end number being added if more balls are being added => less chance for glitchy weird balls, i had it set to 5 for like 4 balls.
                self.speed_x *= -1
                self.speed_y *= -1

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    balls = []

    ball = Ball(screen, (255,0,0), 500,400, 30, 10,10)

    for i in range(4): #red ball will always spawn, so change this number to be 1- the total # of balls you want, ex: 4 will spawn 5 balls
        balls.append(Ball(screen, (random.randint(100,255),random.randint(100,255),random.randint(100,255)), random.randint(100,800),random.randint(100,700), 30, random.randint(3,11),random.randint(3,11)))

    balls.append(ball)


    # TODO: Create an instance of the Ball class called ball1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)

        screen.fill(pygame.Color('black'))

        for ball in balls:
            ball.draw()
            ball.move(balls)



        # TODO: Move the ball
        # TODO: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
