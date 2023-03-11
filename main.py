import pygame, sys, random
from pygame.locals import *

pygame.init()

# Colors
BACKGROUND = (255, 255, 255)
ELEMENTCOLOR = (100, 100, 100)

# GAME Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Create a surface obj with set windows parameters
pygame.display.set_caption("My Game!")

# Main function with game loop
def main():
    running = True

    # Main gameplay loop
    while running:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        
        # Processing
        # Sections will be built out more later

        # Render elements of the game
        GAME_WINDOW.fill(BACKGROUND) # Fill a surface with a solid color 
        # Draw a straight line 
        pygame.draw.line(GAME_WINDOW, ELEMENTCOLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)
        pygame.display.update()
        fpsClock.tick(FPS)
    

    pygame.quit()


if __name__=="__main__":
    main()
