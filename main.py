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
pygame.display.set_caption("PONG!")

# PADDLE Variables
PADDLEINSET = 20
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
BALLSIZE = 10

# Main function with game loop
def main():
    running = True

    left_paddle_y = 50
    right_paddle_y = 50
    ball_X = WINDOW_WIDTH // 2
    ball_Y = WINDOW_HEIGHT // 2

    # Main gameplay loop
    while running:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return
        
        # Processing
        # pygame.Rect obj for holding rect coordinates
        left_paddle_rect = pygame.Rect(PADDLEINSET, left_paddle_y, PADDLEWIDTH, PADDLEHEIGHT)
        right_paddle_rect = pygame.Rect(WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH, right_paddle_y, 
                                        PADDLEWIDTH, PADDLEHEIGHT)

        # Render elements of the game
        GAME_WINDOW.fill(BACKGROUND) # Fill a surface with a solid color 
        # Draw a straight line 
        pygame.draw.line(GAME_WINDOW, ELEMENTCOLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)
        # Draw Rectangle
        pygame.draw.rect(GAME_WINDOW, ELEMENTCOLOR, left_paddle_rect)
        pygame.draw.rect(GAME_WINDOW, ELEMENTCOLOR, right_paddle_rect)
        # Draw ball
        pygame.draw.circle(GAME_WINDOW, ELEMENTCOLOR, (ball_X, ball_Y), BALLSIZE)
        
        pygame.display.update()
        fpsClock.tick(FPS)
    

    pygame.quit()


if __name__=="__main__":
    main()
