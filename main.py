import pygame, sys
from grid import Grid
from blocks import *
from game import Game


# initialize pygame
pygame.init()
dark_blue = (44, 44, 127)




# Create display surface
# Coordinates system (x, y) - (0,0) starts at the top left corner and increasing X as you go right and increasing Y as you go down.
WIDTH = 300
HEIGHT = 600


# Display size for the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Text at the top of the window
pygame.display.set_caption("Python Tetris")


# Speed of the game 
clock = pygame.time.Clock()



# Game loop
# 1. Event handling
# 2. Updating Positions
# 3. Drawing Objects
#  Colors => (RGB) (red, green, blue) i.e (255, 0, 0)

game = Game()


while True:
    for event in pygame.event.get():
        # Handle quiting event -> when user clicks on X button
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move_left()
            elif event.key == pygame.K_RIGHT:
                game.move_right()
            elif event.key == pygame.K_DOWN:
                game.move_down()

            elif event.key == pygame.K_r: 
                game.rotate_block()


    pygame.display.update()
    screen.fill(dark_blue)
    game.draw(screen)
 
    clock.tick(60)
        




